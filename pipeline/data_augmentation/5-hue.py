#!/usr/bin/env python3
"""Task 5"""

import tensorflow as tf


def change_hue(image, delta):
    """Changes the Hue of an Image"""
    altered_image = tf.image.adjust_hue(image, delta)

    return altered_image
