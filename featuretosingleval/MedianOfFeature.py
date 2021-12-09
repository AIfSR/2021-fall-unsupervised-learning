from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from features.Features import Features

class MedianOfFeature (FeatureToSingleValBase):

    def get_val(self, features:Features) -> float:
        """Gets the median value of a feature"""
        sortedListFeature = sorted(features.to_list())
        if len(sortedListFeature) % 2 == 0:
            val1 = sortedListFeature[len(sortedListFeature) // 2]
            val2 = sortedListFeature[len(sortedListFeature) // 2 - 1]
            return (val1 + val2) / 2
        return sortedListFeature[len(sortedListFeature) // 2]

    def __str__(self) -> str:
        return "Median"