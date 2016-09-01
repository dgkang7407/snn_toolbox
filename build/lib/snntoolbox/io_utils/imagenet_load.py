# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 12:55:20 2016

@author: rbodo
"""

# For compatibility with python2
from __future__ import print_function, unicode_literals
from __future__ import division, absolute_import
from future import standard_library

import os
import numpy as np

from keras.preprocessing.image import ImageDataGenerator

standard_library.install_aliases()


def get_imagenet(path, filename=None):
    """
    Load imagenet classification dataset.

    Values are normalized and saved as ``float32`` type. Class vectors are
    converted to binary class matrices. Output can be flattened for use in
    fully-connected networks.

    Parameters
    ----------

    path: string, optional
        If a ``path`` is given, the loaded and modified dataset is saved to
        ``path`` directory.
    filename: string, optional
        Basename of file to create. Individual files will be appended
        ``_X_norm``, ``_X_test``, etc.

    Returns
    -------

    Three compressed files ``path/filename_X_norm.npz``,
    ``path/filename_X_test.npz``, and ``path/filename_Y_test.npz``.
    With data of the form (channels, num_rows, num_cols), ``X_norm`` and
    ``X_test`` have dimension (num_samples, channels, num_rows, num_cols).
    ``Y_test`` has dimension (num_samples, num_classes).

    """

    datagen = ImageDataGenerator()
    dataflow = datagen.flow_from_directory(path, target_size=(224, 224),
                                           batch_size=1000)
    X_test, Y_test = dataflow.next()

#    X_test[:, 0, :, :] -= 103.939
#    X_test[:, 1, :, :] -= 116.779
#    X_test[:, 2, :, :] -= 123.68
#    # 'RGB'->'BGR'
#    X_test = X_test[:, ::-1, :, :]
#    X_test /= 255.

    y_shape = list(Y_test.shape)
    y_shape[-1] = 1000
    print(y_shape)
    y_test = np.zeros(y_shape)
    y_test[:, :102] = Y_test

    if filename is None:
        filename = ''
    filepath = os.path.join(path, filename)
#    np.savez_compressed(filepath + 'X_norm', X_test[::100].astype('float32'))
#    np.savez_compressed(filepath + 'X_test', X_test.astype('float32'))
    np.savez_compressed(filepath + 'Y_test', y_test)

if __name__ == '__main__':
    get_imagenet('/home/rbodo/.snntoolbox/datasets/caltech101/original/')