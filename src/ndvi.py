import rasterio
import numpy as np


def calculate_ndvi(red_band, nir_band):
    ndvi = (nir_band - red_band) / (nir_band + red_band + 1e-10)
    return ndvi


def load_bands(path):
    with rasterio.open(path) as src:
        red = src.read(3).astype(float)
        nir = src.read(4).astype(float)

    return red, nir


if __name__ == "__main__":
    path = "data/sample_satellite.tif"

    red, nir = load_bands(path)

    ndvi = calculate_ndvi(red, nir)

    print("NDVI calculated:", ndvi.shape)