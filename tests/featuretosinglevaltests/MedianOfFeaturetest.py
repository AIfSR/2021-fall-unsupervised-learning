import unittest

from features.Features import Features
from featuretosingleval.MedianOfFeature import MedianOfFeature

class MedianOfFeatureTest(unittest.TestCase):
 
    def test_get_val(self) -> None:
        """Tests getting the max of all the feature values in a feature"""
        lst = [1,2,3,10,5,6,7,9]
        solution = 5.5
        features = Features()
        for val in lst:
            features.add_feature_val(val)
        medianOfFeature = MedianOfFeature()
        self.assertEquals(medianOfFeature.get_val(features), solution)

        lst = [1,8,3,5,6,2,9]
        solution = 5
        features = Features()
        for val in lst:
            features.add_feature_val(val)
        medianOfFeature = MedianOfFeature()
        self.assertEquals(medianOfFeature.get_val(features), solution)
