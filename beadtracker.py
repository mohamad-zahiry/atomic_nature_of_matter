#!/usr/bin/env python3


import numpy as np

from blob import Blob
from beadfinder import bead_finder, get_beads, read_image
from _type_hints import path_list, image_list, beads_pack, beads, distance_list


def read_images(paths: path_list) -> image_list:
    return [read_image(path) for path in paths]


def bulk_bead_finder(images: image_list, tau: int, min_pixels: int) -> beads_pack:
    beads_pack = []
    for img in images:
        blobs = bead_finder(img, tau)
        beads_pack.append(get_beads(min_pixels, blobs, as_numpy=True))

    return np.array(beads_pack, dtype=np.object_)


def __beads_in_delta(beads: beads, bead: Blob, delta: int) -> beads:
    """It returns the beads which in a square with delta width and center of given bead"""
    top = bead + np.array([delta, 0])
    bottom = bead + np.array([-delta, 0])
    right = bead + np.array([0, delta])
    left = bead + np.array([0, -delta])

    beads = beads[beads[:, 0] <= top[0]]
    beads = beads[beads[:, 0] >= bottom[0]]
    beads = beads[beads[:, 1] <= right[1]]
    beads = beads[beads[:, 1] >= left[1]]

    return beads


def __nearest_bead_distance(beads: beads, bead: Blob, delta: int) -> int:
    """If there are more than one bead in delta in the second image,
    we assume the nearest as the bead which we track it"""
    distances = [np.linalg.norm(_bead - bead) for _bead in beads]
    nearest = min(distances)

    if nearest <= delta:
        return nearest


def track_beads(img_1_beads: beads, img_2_beads: beads, delta: int) -> distance_list:
    """It tracks the beads in two consecutive image and returns their displacements
    The img_1_beads and img_2_beads are np_arrays of img1 and img2 found beads"""
    distances = []
    for bead in img_1_beads:

        beads_in_delta = __beads_in_delta(img_2_beads, bead, delta)
        if len(beads_in_delta) == 0:
            continue

        nearest_bead_distance = __nearest_bead_distance(beads_in_delta, bead, delta)

        if nearest_bead_distance:
            distances.append(nearest_bead_distance)

    return distances


def bead_tracker(paths: path_list, tau: int, min_pixels: int, delta: int) -> distance_list:
    """It got a path_list of images and call track_beads for each two consecutive images"""
    images = read_images(paths)
    beads_pack = bulk_bead_finder(images, tau, min_pixels)

    distances = []
    for x in range(len(beads_pack) - 1):
        distances.append(
            track_beads(
                beads_pack[x],
                beads_pack[x + 1],
                delta,
            )
        )

    return distances


def main():
    import sys

    min_pixels, tau, delta, *paths = sys.argv[1:]

    distances = bead_tracker(paths, int(tau), int(min_pixels), int(delta))

    output = ""
    for lst in distances:
        for dist in lst:
            output += "%.4f\n" % dist
        output += "\n"

    print(output, end="")


if __name__ == "__main__":
    main()
