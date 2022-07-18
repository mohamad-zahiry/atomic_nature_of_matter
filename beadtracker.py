#!/usr/bin/env python3


from beadfinder import read_image
from _type_hints import path_list, image_list


def read_images(paths: path_list) -> image_list:
    return [read_image(path) for path in paths]
