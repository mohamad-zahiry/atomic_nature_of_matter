#!/usr/bin/env python3


from typing import List
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

blobs = List[Blob]
beads = np_array[Blob]
beads_pack = np_array[beads]


def read_image(path: path) -> image:
    with Image.open(path) as img:
        gray_img_array = np.asarray(img.convert("L"))
        return np.asarray(gray_img_array)


def apply_threshold(image: image, tau: int) -> image:
    threshold = lambda x, t: 255 if x > t else 0
    vfunc = np.vectorize(threshold)
    return vfunc(image, tau)


def __find_pixels_for_bead(image: image, blobs: blobs, blob: Blob, x: int, y: int) -> None:
    """image : thresholded image
    blobs : list of blobs of the image
    blob  : the blob which we're trying to find its pixels
    x     : x of first pixel of the blob
    y     : y of first pixel of the blob"""

    _x, _y = image.shape

    if (0 > x) or (x >= _x) or (0 > y) or (y >= _y) or (image[x][y] == 0):
        return

    blob.add(x, y)

    # Change found pixels to 0. So, __find_beads don't
    # use them for new blob in the next its iteration.
    image[x][y] = 0

    __find_pixels_for_bead(image, blobs, blob, x + 1, y)  # top
    __find_pixels_for_bead(image, blobs, blob, x + 1, y + 1)  # top-right
    __find_pixels_for_bead(image, blobs, blob, x, y + 1)  # right
    __find_pixels_for_bead(image, blobs, blob, x - 1, y + 1)  # bottom-right
    __find_pixels_for_bead(image, blobs, blob, x - 1, y)  # bottom
    __find_pixels_for_bead(image, blobs, blob, x - 1, y - 1)  # bottom-left
    __find_pixels_for_bead(image, blobs, blob, x, y - 1)  # left
    __find_pixels_for_bead(image, blobs, blob, x - 1, y - 1)  # top-left


def __find_beads(image: image, blobs: blobs) -> None:
    xs, ys = np.where(image == 255)

    # All found pixels are change to 0 by __find_pixels_for_bead,
    # So in next iteration, they aren't used for a new blob.
    for x in xs:
        for y in ys:
            if image[x][y] == 255:
                blob = Blob()
                blobs.append(blob)
                __find_pixels_for_bead(image, blobs, blob, x, y)
