import os
from time import clock
from SavingNumpyImage import SavingImageAsNumpy
from readNumpyImage import ReadNumpy

__author__ = 'Agnieszka'

import numpy as np
import multiprocessing as mp


class LocalExterma3D(object):
    def __init__(self, path):
        """
        Find local extrema without edges in one image
        """
        self.true_array = np.ones((3, 3, 3), dtype=np.bool)
        self.false_array = -self.true_array
        self.true_array[1, 1, 1] = False

        self.min_list = []
        self.max_list = []
        self.path = path
        self.ReadImage = ReadNumpy(path)

    def find_one(self, image3D):
        """
        :param image3D: image after convolution LoG
        :return: void
        """
        self.min_list = []
        self.max_list = []
        shape = image3D.shape
        start = clock()
        for i in range(1, shape[0]):

            for j in range(1, shape[1]):
                for z in range(1, shape[2]):
                    bool_array = image3D[i, j, z] > image3D[i - 1:i + 2, j - 1:j + 2, z - 1:z + 2]
                    sum = np.sum(bool_array)
                    if sum == 0:
                        self.max_list.append(np.array([i, j, z]))
                    elif sum == 26 and bool_array[1, 1, 1] == False:
                        self.min_list.append(np.array([i, j, z]))


        end = clock() - start

        print end

    def find(self):

        list_with_images = self.ReadImage.openImage()
        path_to_save = '/3DLocalExteremum/'
        try:
            os.makedirs(self.path + path_to_save)
        except OSError:
            pass
        saving = SavingImageAsNumpy(self.path + path_to_save)
        for i in range(0, len(list_with_images)):
            self.find_one(list_with_images[i])
            min3D, max3D = self.get_min_max()
            saving.saveIndex(min3D, max3D, self.ReadImage.sigmas_images[i])
            print('image nr' + str(i) + 'done')


    def get_min_max(self):
        """
        :return: list of indexes as a np.array min and max [i,j,z]
        """
        return np.array(self.min_list), np.array(self.max_list)