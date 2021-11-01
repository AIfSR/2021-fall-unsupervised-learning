from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class MaxMinDifferenceOfFeature (FeatureCreatorBase):
    """Creates a feature with a single value that is the range of the original 
    feature"""
    def __init__(self, origFeatureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._origFeatureCreator = origFeatureCreator

    def get_features(self, points:Points) -> Features:
        """Gets all the range of feature vals"""
        origFeatures = self._origFeatureCreator.get_features(points)
        features = Features()
        featureValList = origFeatures.to_list()
        features.add_feature_val(max(featureValList) - min(featureValList))
        return features

    def __str__(self) -> str:
        """This is a feature for range"""
        return "Range:" + str(self._origFeatureCreator)