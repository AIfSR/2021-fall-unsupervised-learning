import unittest

from features.Features import Features
from featuretosingleval.AverageOfFeature import AverageOfFeature

class AverageOfFeatureTest(unittest.TestCase):
 
    def test_get_val(self) -> None:
        """Tests getting the average of all the feature values in a feature"""
        lst = [1,2,3,4,5,6,7,7]
        solution = sum(lst) / len(lst)
        features = Features()
        for val in lst:
            features.add_feature_val(val)
        averageOfFeature = AverageOfFeature()
        self.assertEquals(averageOfFeature.get_val(features), solution)
