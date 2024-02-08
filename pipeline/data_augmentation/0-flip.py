#!/usr/bin/env python3
"""Task 0"""

import tensorflow as tf


def flip_image(image):
    """Flips an Image Horizontally"""
    flipped_image = tf.image.flip_left_right(image)

    return flipped_image
