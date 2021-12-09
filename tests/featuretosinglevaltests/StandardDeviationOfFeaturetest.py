import unittest

from features.Features import Features
from featuretosingleval.StandardDeviationOfFeature import StandardDeviationOfFeature

class StandardDeviationOfFeatureTest(unittest.TestCase):
 
    def test_get_val(self) -> None:
        """Tests getting the standard deviation of all the feature values in a feature"""
        lst = [3,6,9]
        solution = 6**0.5
        features = Features()
        for val in lst:
            features.add_feature_val(val)
        standardDeviationOfFeature = StandardDeviationOfFeature()
        self.assertEquals(standardDeviationOfFeature.get_val(features), solution)
