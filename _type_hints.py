#!/usr/bin/env python3


"""All type which used in this project are stored here"""

from typing import List

import numpy as np
import numpy.typing as npt

from blob import Blob


np_array = npt.ArrayLike

path = str
path_list = List[path]

image = np_array
image_list = List[image]

blobs = List[Blob]
beads = np_array[Blob]
beads_pack = np_array[beads]

distance = int
distance_list = np_array[distance]
