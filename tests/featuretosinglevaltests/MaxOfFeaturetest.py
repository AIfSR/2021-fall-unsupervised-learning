import unittest

from features.Features import Features
from featuretosingleval.MaxOfFeature import MaxOfFeature

class MaxOfFeatureTest(unittest.TestCase):
 
    def test_get_val(self) -> None:
        """Tests getting the max of all the feature values in a feature"""
        lst = [1,2,3,10,5,6,7,9]
        solution = 10
        features = Features()
        for val in lst:
            features.add_feature_val(val)
        maxOfFeature = MaxOfFeature()
        self.assertEquals(maxOfFeature.get_val(features), solution)
