#!/usr/bin/env python3
"""Task 1"""

import tensorflow as tf


def crop_image(image, size):
    """Crops an Image"""
    cropped_image = tf.image.random_crop(image, size)

    return cropped_image
