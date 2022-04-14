"""Lab 10 task 3"""
from arrays import Array2D
import numpy as np
from PIL import Image, ImageOps
from image_compress import LZW
import os


class GrayscaleImage:
    """Class for black-white pictures
    >>> im1 = GrayscaleImage(10, 10)
    >>> im1.clear(60)
    >>> im1.height()
    10
    >>> im1._grid[0, 1]
    60
    >>> im1.getitem(0, 1)
    60
    >>> im1.setitem(0, 1, 100)
    >>> im1.getitem(0, 1)
    100
    """
    def __init__(self, nrows, ncols):
        """The constructor for this class"""
        self.nrows = nrows
        self.ncols = ncols
        self._grid = Array2D(nrows, ncols)

    def width(self):
        """
        This function returns the number of pixels columns
        in picture
        """
        return self.ncols

    def height(self):
        """
        This function returns the number of pixels rows
        in picture
        """
        return self.nrows

    def clear(self, value):
        """
        This function make all pixels of picture
        the intensity that given
        """
        if 0 <= value <= 255:
            for i in range(self.nrows):
                for j in range(self.ncols):
                    self._grid[i, j] = value

    def getitem(self, row, col):
        """
        This function returns the intensity of pixel
        """
        if 0 <= row < self.nrows and 0 <= col < self.ncols:
            return self._grid[row, col]

    def setitem(self, row, col, value):
        """
        This function makes the pixel to given intensity
        """
        if 0 <= row < self.nrows and 0 <= col < self.ncols and 0<=value<=255:
            self._grid[row, col] = value

    @staticmethod
    def from_file(path):
        """
        This function make class object from jpg file
        """
        image = Image.open(path)
        col, rows = image.size
        new_im = GrayscaleImage(rows, col)
        new_im._grid = np.array(ImageOps.grayscale(image))
        # file = open("1.lzw", "w")
        # for i in range(new_im.height()):
        #     for j in range(new_im.width()):
        #         file.write(str(new_im._grid[i, j])+",")
        #     file.write("\n")
        # file.close()
        return new_im
        
    def lzw_compression(self, name="first"):
        """
        This function compress the class's object with lzw
        methods and save result in folder "Compressed files"
        """
        array = []
        for i in range(self.height()):
            array.append([])
            for j in range(self.width()):
                array[i].append(self._grid[i, j])
        # print(array[:10])
        mat = np.reshape(array,(self.height(), self.width()))
        img = Image.fromarray(mat)
        img.show()
        img.save(os.path.join("Images",f"{name}.tiff"))
        
        compressor = LZW(os.path.join("Images",f"{name}.tiff"))
        compressor.compress()

    def lzw_decompression(self, name="first"):
        """
        This function decompress the lzw files
        and save result in folder "Decompressed files"
        """
        decompressor = LZW(os.path.join("CompressedFiles",f"{name}Compressed.lzw"))
        decompressor.decompress()
        
# im1 = GrayscaleImage(10, 10)
# im1.clear(60)
# # for i in range(5, im1.height()-2):
# #     for j in range(2, im1.width()):
# #         im1.setitem(i, j, 250)
# im2 = GrayscaleImage.from_file(os.path.join("Images","first.jpg"))
# # for i in range(im2.height()):
# #     for j in range(im2.width()):
# #         print(im2._grid[i, j])
# im2.lzw_decompression("file_")
# # for i in range(im1.height()):
# #     for j in range(im1.width()):
# #         print(im2._grid[i, j])

# import doctest
# doctest.testmod()
