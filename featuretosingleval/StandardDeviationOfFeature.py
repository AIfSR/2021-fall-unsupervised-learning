from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from featuretosingleval.AverageOfFeature import AverageOfFeature
from features.Features import Features

class StandardDeviationOfFeature (FeatureToSingleValBase):

    def __init__(self) -> None:
        self.averageOfFeature = AverageOfFeature()

    def get_val(self, features:Features) -> float:
        """Gets the standard deviation of a feature"""
        avg = self.averageOfFeature.get_val(features)
        sum = 0
        count = 0
        for featureVal in features:
            sum += (featureVal - avg)**2
            count +=1
        stdDev = (sum/count)**0.5
        return stdDev

    def __str__(self) -> str:
        return "Standard Deviation"
