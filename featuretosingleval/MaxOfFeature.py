from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from features.Features import Features

class MaxOfFeature (FeatureToSingleValBase):

    def get_val(self, features:Features) -> float:
        """Gets the maximum value of a feature"""
        return max(features)
