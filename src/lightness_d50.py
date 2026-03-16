import colour

from råsa import RÅSA_XYZ


def lightness_d50_measurements():
    d65_xy = colour.CCS_ILLUMINANTS["CIE 1931 2 Degree Standard Observer"]["D65"]
    d50_xy = colour.CCS_ILLUMINANTS["CIE 1931 2 Degree Standard Observer"]["D50"]

    d65_XYZ = colour.xy_to_XYZ(d65_xy)
    d50_XYZ = colour.xy_to_XYZ(d50_xy)

    råsa_xyz_d50 = colour.chromatic_adaptation(
        RÅSA_XYZ,
        d65_XYZ,
        d50_XYZ,
    )

    råsa_cie_lab_d50 = colour.models.cie_lab.XYZ_to_Lab(råsa_xyz_d50, illuminant=d50_xy)
    råsa_cie_luv_d50 = colour.models.cie_luv.XYZ_to_Luv(råsa_xyz_d50, illuminant=d50_xy)

    print("CIE Lab Lightness", 100 - råsa_cie_lab_d50[0])
    print("CIE Luv Lightness", 100 - råsa_cie_luv_d50[0])
