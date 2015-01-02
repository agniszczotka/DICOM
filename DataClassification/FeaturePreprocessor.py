import os
from numpy import array, concatenate
from IOSift.FeatureReader import FeatureReader

__author__ = 'Agnieszka'


class FeaturePreprocessor():
    def __init__(self, path):
        self.path = path
        self.list_with_features_object = {}
        self.list_with_features_object['prostate'] = []
        self.list_with_features_object['bladder'] = []
        self.list_with_features_object['rectum'] = []
        self.list_with_features_object['femurR'] = []
        self.list_with_features_object['femurL'] = []
        self.list_with_features_object['semi_vesicle'] = []
        self.organs_names = ['rectum', 'prostate', 'bladder', 'femurL', 'femurR', 'semi_vesicle']

    def apply(self):

        path = '/CT_analysesClassification/'

        for i in range(1, 4):
            i=1
            try:
                path = self.path+'/'+ str(i) + '_nd//CT_analysesClassification/'
                if not os.path.exists(path):
                    raise IOError
            except IOError:
                continue
            for o in range(1, 4):
                path_temp = path + str(o) + '/FullFeature/'
                print(path_temp)
                feature_list = FeatureReader(path_temp).open()
                for feature in feature_list:
                    for orgnas in self.organs_names:
                        if eval('feature.'+orgnas+'_keypoints.size') != 0:
                            for e in eval('feature.'+orgnas+'_keypoints'):
                                self.list_with_features_object[orgnas].append(e[3:])


    def get_feature(self):
        dic_temp = {}
        for orgnas in self.organs_names:
            dic_temp[orgnas] = array(self.list_with_features_object[orgnas])

        return dic_temp

    def get_data_for_classificator(self):
        data=self.get_feature()
        #for e in data