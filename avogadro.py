#!/usr/bin/env python3


import numpy as np

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


def boltzmann(D):
    """
    boltzmann constant (aka: K)
    D: self-diffusion coefficient

    D = (K T) / (6 PI RHO ETA)
    K = (6 D PI RHO ETA) / T
    """
    T = 297
    PI = np.pi
    ETA = 9.135e-4
    RHO = 0.5e-6
    return (6 * D * PI * RHO * ETA) / T


def avogadro(K):
    """
    avogadro constant (aka: NA): number of units in one mole of any substance
    K: boltzmann constant

    K = R / NA
    NA = R / K
    """
    R = 8.31446
    return R / K


def main():
    import sys

    displacements = sys.stdin.read().split("\n")
    displacements = list(filter(None, displacements))
    displacements = list(map(float, displacements))

    self_diffusion = sdc(displacements)
    boltzmann_constant = boltzmann(self_diffusion)
    avogadro_constant = avogadro(boltzmann_constant)

    print("Boltzmann = %.4e" % boltzmann_constant)
    print("Avogadro = %.4e" % avogadro_constant)


if __name__ == "__main__":
    main()
