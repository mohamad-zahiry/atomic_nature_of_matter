#!/usr/bin/env python3


from PIL import Image
import numpy as np
import numpy.typing as npt

from blob import Blob


"""
The types that used in this module.
"""
np_array = npt.ArrayLike

path = str

image = np_array


def read_image(path: path) -> image:
    with Image.open(path) as img:
        gray_img_array = np.asarray(img.convert("L"))
        return np.asarray(gray_img_array)


def apply_threshold(image: image, tau: int) -> image:
    threshold = lambda x, t: 255 if x > t else 0
    vfunc = np.vectorize(threshold)
    return vfunc(image, tau)
