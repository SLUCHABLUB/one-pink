import numpy
from colour import models, notation

from significant_digits import find_minimum_significant_digits


def hex_sRGB_to_Oklab(hex):
    return models.XYZ_to_Oklab(models.sRGB_to_XYZ(notation.HEX_to_RGB(hex)))


def Oklab_to_hex_sRGB(colour):
    return notation.RGB_to_HEX(models.XYZ_to_sRGB(models.Oklab_to_XYZ(colour)))


RÅSA_HEX = "#f280a1"
RÅSA_OKLAB = hex_sRGB_to_Oklab(RÅSA_HEX)


def main():
    find_minimum_significant_digits()


if __name__ == "__main__":
    main()
