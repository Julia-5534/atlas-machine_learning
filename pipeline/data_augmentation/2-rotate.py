#!/usr/bin/env python3
"""Task 2"""

import tensorflow as tf


def rotate_image(image):
    """Rotate an Image by 90 degrees counter-clockwise"""
    rotated_image = tf.image.rot90(image)

    return rotated_image
