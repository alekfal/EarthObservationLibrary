# Title: Read a raster with rasterio
# Name: Falagas Alekos
# Location: RSLab, SRSE-NTUA, 2019
# e-mail: alek.falagas@gmail.com
# Version: 0.0.6

import rasterio
import os
import sys
import numpy as np

class earthobspy:
    """Collection of methods for raster manipulation based on rasterio"""
    
    @staticmethod
    def datatypes(dtp):
        """ A method that returns the code of datatype.

        Args:
            dtp (dict): A dictonary with the valid datatypes and codes

        Returns:
            int: The valid datatype code
        """

        dtype_fwd = {None: 0, #GDT_Unknown
            'uint8': 1, #GDT_Byte
            'ubyte': 1, #GDT_Byte
            'uint16': 2, #GDT_UInt16
            'int16': 3, #GDT_Int16
            'uint32': 4, #GDT_UInt32
            'int32': 5, #GDT_Int32
            'float32': 6, #GDT_Float32
            'float64': 7, #GDT_Float64
            'complex_': 8, #GDT_CInt16
            'complex_': 9, #GDT_CInt32
            'complex64': 10, #GDT_CFloat32
            'complex128': 11} #GDT_CFloat64

        return (dtype_fwd[dtp])

    @staticmethod
    def metadata(path, name,  verbose = False):
        """A method to read raster file metadata.

        Args:
            path (str, path-like): Path to file
            name (str): File name
            verbose (bool, optional): If True prints information about the raster data. Defaults to False

        Returns:
            tuple: Returns metadata about the raster
        """
        image = rasterio.open(os.path.join(path, name))
        crs = image.crs
        bands = image.count
        up_l_crn = image.transform * (0, 0)
        pixel_size = image.transform[0]
        nodata = image.nodata
        width = image.width
        height = image.height
        dtps = image.dtypes
        dtp_code= []
        for dtp in dtps:
            dtp_code.append(earthobspy.datatypes(dtp))
            if verbose == True:
                print ('Data Type: {} - {}'.format(dtp, dtp_code))
        driver = image.driver
        utm = crs.wkt

        # Print results if True
        if verbose == True:
            print ('CRS: {}'.format(crs))
            print ('Bands: {}'.format(bands))
            print ('Upper Left Corner: {}'.format(up_l_crn))
            print ('Pixel size: {}'.format(pixel_size))
            print ('Width: {}'.format(width))
            print ('Height: {}'.format(height))
            print (driver)
            print ('UTM Zone: {}'.format(utm))

        return (crs, bands, up_l_crn, pixel_size, width, height, dtps, dtp_code, driver, utm, nodata)

    @staticmethod
    def readraster(path, name, bands = -1):
        """A method to read raster files.
            Default values: bands = -1 -> read all bands

        Args:
            path (str, path-like): Path to file
            name (str): File name
            bands (int, optional): Reads a specific band to memory, else reads the whole raster (-1). Defaults to -1

        Returns:
            tuple: Returns the image as rasterio object, the array as ndarray and more metadata about the raster
        """
        print ('Trying to read raster file...')
        print ('Reading file {}.'.format(name))
        # Reading data with rasterio
        image = rasterio.open(os.path.join(path, name))
        crs, count, up_l_crn, pixel_size, width, height, dtps, dtp_code, driver, utm, nodata = earthobspy.metadata(path, name)
        transform = image.transform

        # Getting all Bands
        if bands == -1:
                array = image.read()
        else:
            array = image.read(bands)
        print ('Done!')
        return (image, array, crs, count, up_l_crn, pixel_size, width, height, dtps, dtp_code, driver, utm, transform, nodata)

    @staticmethod
    def writeraster(path, name, array, width, height, crs, transform, nodata = None, dtype = (rasterio.float32,), ext = 'Gtiff'):
        print ('Trying to write raster data...')
        # Checking if there are more than 1 dtypes and dtype is a list
        if len(dtype) > 0 and isinstance(dtype, tuple):
            # Checking for unique values in case of multiband image
            unique = list(set(dtype))
            if len(unique) > 0:
                fdtype = unique[0]
                for u in unique:
                    if earthobspy.datatypes(fdtype) < earthobspy.datatypes(u):
                        fdtype = u
            else:
                fdtype = dtype
        else:
            print ('Something is wrong with datatypes. Try to use readraster(...) to open the image.')
            sys.exit(1)

        #Checking if user's datatype matches with array's datatype
        if len(array.shape) == 3:
            for i in range(len(array)):
                if array[i, :, :].dtype != fdtype:
                    print ("Found difference in array's datatype and user's datatype.")
                    print ("Replacing datatype {} with {}.".format(fdtype, array[i, :, :].dtype))
                    fdtype = array[i, :, :].dtype
        else:
            if array.dtype != fdtype:
                print ("Found difference in array's datatype and user's datatype.")
                print ("Replacing datatype {} with {}.".format(fdtype, array.dtype))
                fdtype = array.dtype

        # Multiband images
        if len(array.shape) == 3:
            if nodata == None:
                bands=rasterio.open(os.path.join(path, name),'w',driver=ext,width=width, height=height,
                    count = len(array),
                    crs = crs,
                    transform = transform,
                    dtype = fdtype)
            else:
                bands=rasterio.open(os.path.join(path, name),'w',driver=ext,width=width, height=height,
                    count = len(array),
                    crs = crs,
                    transform = transform,
                    dtype = fdtype,
                    nodata = nodata)
            for b in range(len(array)):
                bands.write(array[b,:,:], b+1)
            bands.close()
        # Singleband image
        else:
            if nodata == None:
                bands=rasterio.open(os.path.join(path, name),'w',driver=ext,width=width, height=height,
                    count = 1,
                    crs = crs,
                    transform = transform,
                    dtype = fdtype)
            else:
                bands=rasterio.open(os.path.join(path, name),'w',driver=ext,width=width, height=height,
                    count = len(array),
                    crs = crs,
                    transform = transform,
                    dtype = fdtype,
                    nodata = nodata)
            bands.write(array, 1)
            bands.close()
        print ('Raster saved as {}!'.format(name))

    @staticmethod
    def split_bands(path, name, verbose = False):
        """A method to split multiband raster data to single images.

        Args:
            path (str, path-like): Path to file
            name (str): File name
            verbose (bool, optional): If True prints information about the process. Defaults to False
        """
        # Reading data with rasterio
        image = rasterio.open(os.path.join(path, name))
        # Getting image name without extension
        name_we = os.path.splitext(name)[0]
        for b in range(1, (image.count+1)):
            filename = name_we + '_band_{}.tif'.format(b)
            if verbose == True:
                print ('Trying to save band {} as {}'.format(b, filename))
            band=rasterio.open(os.path.join(path, filename),'w',driver = 'Gtiff',width = image.width, height=image.height, count = 1, crs = image.crs, transform = image.transform, dtype=image.read(b).dtype)
            band.write(image.read(b), 1)
            band.close()
            if verbose == True:
                print('Done!')
