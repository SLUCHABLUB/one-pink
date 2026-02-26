import colour

RÅSA_HEX = "F280A1"
RÅSA_SRGB = colour.notation.HEX_to_RGB(RÅSA_HEX)
RÅSA_XYZ = colour.models.sRGB_to_XYZ(RÅSA_SRGB)
RÅSA_OKLAB = colour.models.XYZ_to_Oklab(RÅSA_XYZ)


def main():
    print(RÅSA_OKLAB)


if __name__ == "__main__":
    main()
