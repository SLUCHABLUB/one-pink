from lightness_d50 import lightness_d50_measurements
from pantone import pantone_diffs
from significant_digits import find_minimum_significant_digits
from råsa import RÅSA_OKLAB


def main():
    print(RÅSA_OKLAB)
    find_minimum_significant_digits()
    print()
    lightness_d50_measurements()
    print()
    pantone_diffs()


if __name__ == "__main__":
    main()
