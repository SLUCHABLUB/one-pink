import numpy

from main import RÅSA_HEX, RÅSA_OKLAB, Oklab_to_hex_sRGB


def round_significant_digits(value, digits):
    string = numpy.format_float_positional(
        value, precision=digits, unique=False, fractional=False, trim="k"
    )

    return numpy.float64(string)


round_significant_digits_vector = numpy.vectorize(round_significant_digits)


def find_minimum_significant_digits():
    for significant_digits in range(8, 0, -1):
        rounded = round_significant_digits_vector(RÅSA_OKLAB, significant_digits)

        hex = Oklab_to_hex_sRGB(rounded)

        status = "OK" if hex == RÅSA_HEX else "BAD"

        print(
            f"{significant_digits} sig. digits gives {rounded} which becomes {hex}: {status}"
        )
