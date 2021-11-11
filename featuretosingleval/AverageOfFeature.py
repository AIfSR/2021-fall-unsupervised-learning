from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from features.Features import Features

class AverageOfFeature (FeatureToSingleValBase):

    def get_val(self, features:Features) -> float:
        """Gets the average of a feature"""
        count = 0
        sum = 0
        for featureVal in features:
            sum += featureVal
            count += 1
        return sum / count
