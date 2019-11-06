# EarthObservationLibrary
Simple python functions for raster manipulation.

### Functions
------------------------------------------------
#### readraster:
Inputs: 
* path (String, path to file)
* name (String, name of the file)
* bands (default value = -1, read all bands)

Outputs:
* image (rasterio object)
* array (numpy array, the array from the raster)
* crs (String)
* count (Integer)
* up_l_crn (Tuple)
* pixel_size (Integer)
* width (Integer)
* height (Integer)
* dtps (Tuple)
* dtp_code (Tuple)
* driver (String)
* utm (String)
* transform (String)

####  writeraster:
Inputs: 
* path (String, path to file)
* name (String, name of the file)
* array (numpy array, the array from the raster)
* width (Integer)
* height (Integer)
* crs (String)
* transform (String)
* dtype (Tuple, default value = (rasterio.float32,))
* ext (String, default value = 'Gtiff')

Outputs:
* Raster file to the selected path.

#### Other functions:

split_bands (Spliting a multiband image to singleband images), metadata, datatypes

------------------------------------------------
### Required Python Libraries
------------------------------------------------
#### rasterio
Install with pip:
$ pip install rasterio

#### numpy
Install with pip:
$ pip install numpy

------------------------------------------------

