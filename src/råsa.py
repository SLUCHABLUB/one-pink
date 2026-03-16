from colour import models, notation


def hex_sRGB_to_Oklab(hex):
    return models.XYZ_to_Oklab(models.sRGB_to_XYZ(notation.HEX_to_RGB(hex)))


def Oklab_to_hex_sRGB(colour):
    return notation.RGB_to_HEX(models.XYZ_to_sRGB(models.Oklab_to_XYZ(colour)))


RÅSA_HEX = "#f280a1"
RÅSA_sRGB = notation.HEX_to_RGB(RÅSA_HEX)
RÅSA_XYZ = models.sRGB_to_XYZ(RÅSA_sRGB)
RÅSA_OKLAB = models.XYZ_to_Oklab(RÅSA_XYZ)
RÅSA_CIE_LAB = models.cie_lab.XYZ_to_Lab(RÅSA_XYZ)
