#!/usr/bin/env python3
"""Task 3"""

import tensorflow as tf
tf.experimental.numpy.experimental_enable_numpy_behavior()


def shear_image(image, intensity):
    """Shears an Image"""
    sheared_image = tf.keras.preprocessing.image.random_shear(image,
                                                              intensity,
                                                              row_axis=1,
                                                              col_axis=0,
                                                              channel_axis=2)

    return sheared_image
