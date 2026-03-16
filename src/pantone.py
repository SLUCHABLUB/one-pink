import colour
import numpy

from råsa import RÅSA_CIE_LAB, RÅSA_HEX, RÅSA_OKLAB
from significant_digits import round_significant_digits

CANDIDATES = {
    "`#f280a1`": RÅSA_HEX,
    "Pantone 204 U": "EE82A4",
    "Pantone 6051 U": "FE7C9E",
    "Pantone 190 U": "FE87A3",
    "Pantone 2038 U": "F372A6",
    "Pantone 4072 U": "E47E97",
    "Pantone 701 U": "E98F9D",
    "Pantone 1775 U": "FF8B9A",
    "Pantone 183 U": "FF8DA3",
    "Pantone 189 U": "FFABC2",
}


def pantone_diffs():
    for name, candidate_hex in CANDIDATES.items():
        candidate_srgb = colour.notation.HEX_to_RGB(candidate_hex)
        candidate_xyz = colour.models.sRGB_to_XYZ(candidate_srgb)
        candidate_oklab = colour.models.XYZ_to_Oklab(candidate_xyz)
        candidate_cie_lab = colour.models.cie_lab.XYZ_to_Lab(candidate_xyz)

        l2_oklab = numpy.linalg.norm(candidate_oklab - RÅSA_OKLAB)

        delta_e_00 = (
            colour.delta_E(candidate_cie_lab, RÅSA_CIE_LAB, method="CIE 2000") / 100
        )
        delta_e_94 = (
            colour.delta_E(candidate_cie_lab, RÅSA_CIE_LAB, method="CIE 1994") / 100
        )
        delta_e_76 = (
            colour.delta_E(candidate_cie_lab, RÅSA_CIE_LAB, method="CIE 1976") / 100
        )

        print(
            name,
            candidate_hex,
            round_significant_digits(l2_oklab, 3),
            round_significant_digits(delta_e_00, 3),
            round_significant_digits(delta_e_94, 3),
            round_significant_digits(delta_e_76, 3),
        )
