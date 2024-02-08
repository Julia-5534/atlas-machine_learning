#!/usr/bin/env python3
"""Task 4"""

import tensorflow as tf


def change_brightness(image, max_delta):
    """Changes the Brightness of an Image"""
    altered_image = tf.image.adjust_brightness(image, max_delta)

    return altered_image
