from earthobspy.earthobspy import Pyearthobs
import numpy as np

def Test_read_write(path, raster):
    "A function that multiplies every band with 1000"
    # Test read data
    image, array, crs, bands, up_l_crn, pixel_size, rows, cols, dtps, dtp_code, driver, utm, transform = Pyearthobs.readraster(path, raster)
    # Procecssing
    new_array = np.zeros(array.shape)
    for b in range(array.shape[0]):
        new_array[b,:,:] = (array[b,:,:] * 1000)
    # Writing data
    raster = raster.split(".")[0] + "_1000.tif"
    Pyearthobs.writeraster(path, raster, new_array, rows, cols, crs, transform, ('float32',))

    return True

def Test_split(path, raster):
    Pyearthobs.split_bands(path, raster, verbose = False)
    return True

if __name__ == "__main__":
    result = Test_read_write("./Test/", "test_data.tif")
    print(result)

    result = Test_split("./Test/", "test_data.tif")
    print(result)