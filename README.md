# EarthObservationLibrary

Collection of python functions for raster manipulation.



### Required Python Libraries

------------------------------------------------

#### rasterio
Install with pip3: ```$pip3 install rasterio```

#### numpy
Install with pip3: ```$pip3 install numpy```



### Functions

------------------------------------------------

#### readraster

A simple function to read raster files. Uses function metadata() for getting information about the image.
    
 ```   

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * bands - Default values: bands = -1 (read all bands). For reading for example the first 2 bands of a
      multiband use variable bands as: bands = (1, 2). To read 1 band just provide the corresponding band number

Outputs:

    * image - The image as a rasterio object
    * array - The image as a np.array
    * all the metadata from function metadata()

```

####  writeraster

Write a new raster with rasterio.

```

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * array - The image as a np.array (np.array)
    * width - Number of columns (Integer)
    * height - Number of rows (Integer)
    * crs - Coordinates Reference System (String)
    * transform - Image transform (Tuple)
    * dtype - Image datatype (Optional, default value = (rasterio.float32,)). In case of difference in array's datatype and user's datatype
      the script will save data with array's datatype (tuple)
    * ext - Extension (Optional, default value = 'Gtiff') (string)

Outputs:
    
    * Raster file to selected path 

```

#### metadata

A simple function to read raster file metadata.

```

Inputs:

    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * verbose - Printing results (Optional, default value = False) (bool)

Outputs:

    * crs - Coordinates Reference System (String)
    * bands - Number of bands (Integer)
    * up_l_crn - Upper left corner coordinates (Tuple)
    * pixel_size - Pixel size (Integer)
    * width - Number of columns (Integer)
    * height - Number of rows (Integer)
    * dtps - Image's datatype (Tuple)
    * dtp_code - Datatype's code (Tuple)
    * driver - Image's driver (String)
    * utm - Image's CRS in WKT (String)
    * transform - Image's transform (Tuple)

```

#### split_bands

A simple function to split multiband raster data to single images.
    
```

Inputs:
    
    * path - Path to raster file (string)
    * name - Name of the raster file (string)
    * name_ext - New name extension (Optional, default value = '_band_') (string)
    * verbose - Printing results (Optional, default value = False) (bool)
    
Outputs:

    * Raster files to selected path

```
