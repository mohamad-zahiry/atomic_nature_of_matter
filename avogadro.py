#!/usr/bin/env python3


METER_PER_PIXEL = 0.175e-6


def sdc(displacements, delta_t=0.5):
    """
    self-diffusion coefficient (aka: D)
    delta_t: time delta in seconds

    variance = 2 D delta_t
    D = variance / (2 delta_t)
    """
    n = len(displacements)
    variance = sum(list(map(lambda x: (x * METER_PER_PIXEL) ** 2, displacements))) / (2 * n)
    return variance / (2 * delta_t)
