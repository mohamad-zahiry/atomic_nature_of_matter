#!/usr/bin/env python3


import numpy as np

from beadfinder import bead_finder, get_beads, read_image
from _type_hints import path_list, image_list, beads_pack


def read_images(paths: path_list) -> image_list:
    return [read_image(path) for path in paths]


def bulk_bead_finder(images: image_list, tau: int, min_pixels: int) -> beads_pack:
    beads_pack = []
    for img in images:
        blobs = bead_finder(img, tau)
        beads_pack.append(get_beads(min_pixels, blobs, as_numpy=True))

    return np.array(beads_pack, dtype=np.object_)
