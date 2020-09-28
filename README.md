# EarthObservationLibrary

Collection of python methods for raster manipulation.



### Required Python Libraries

------------------------------------------------

```
rasterio>=1.1.2
numpy>=1.18.5
```

### Installation

------------------------------------------------

```bash
git clone https://github.com/alekfal/EarthObservationLibrary.git
cd EarthObservationLibrary
pip install .
```
### Example

------------------------------------------------

```python
from earthobspy import earthobspy
import numpy as np

# Read data
image, array, crs, bands, up_l_crn, pixel_size, rows, cols, dtps, dtp_code, driver, utm, transform = earthobspy.readraster(path, raster)

# Processing (multiply every array * 1000)
new_array = np.zeros(array.shape)
for b in range(array.shape[0]):
    new_array[b,:,:] = (array[b,:,:] * 1000)

# Writing data
raster = raster.split(".")[0] + "_1000.tif"
earthobspy.writeraster(path, raster, new_array, rows, cols, crs, transform, dtype = ('float32',), nodata = 0)

```

### Methods

------------------------------------------------

#### readraster

A method to read raster files. Uses static method metadata() for getting information about the image.

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * bands - Default values: bands = -1 (read all bands). For reading for example the first 2 bands of a
      multiband use variable bands as: bands = (1, 2). To read 1 band just provide the corresponding band number

Outputs:

    * image - The image as a rasterio object
    * array - The image as a np.array
    * all the metadata from function metadata()


####  writeraster

Write a new raster with rasterio.

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * array - The image as a np.array (np.array)
    * width - Number of columns (integer)
    * height - Number of rows (integer)
    * crs - Coordinates Reference System (string)
    * transform - Image transform (tuple)
    * dtype - Image datatype (Optional, default value = (rasterio.float32,)). In case of difference in array's datatype and user's datatype
      the script will save data with array's datatype (tuple)
    * ext - Extension (Optional, default value = 'Gtiff') (string)
    * nodata - No data value (Optional, default value = None) (numeric)

Outputs: 

    * Raster file to selected path 

#### metadata

A method to read raster file metadata.

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * verbose - Printing results (Optional, default value = False) (bool)

Outputs:

    * crs - Coordinates Reference System (string)
    * bands - Number of bands (integer)
    * up_l_crn - Upper left corner coordinates (tuple)
    * pixel_size - Pixel size (integer)
    * width - Number of columns (integer)
    * height - Number of rows (integer)
    * dtps - Image's datatype (tuple)
    * dtp_code - Datatype's code (tuple)
    * driver - Image's driver (string)
    * utm - Image's CRS in WKT (string)
    * nodata - No data value of input image (numeric)

#### split_bands

A simple function to split multiband raster data to single images.

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * verbose - Printing results (Optional, default value = False) (bool)
    
Outputs:

    * Raster files to selected path