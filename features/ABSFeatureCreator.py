from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class ABSFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the absolute value of the feature creator 
    passed in"""
    def __init__(self, featureCreatorBase:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreatorBase = featureCreatorBase

    def get_features(self, points:Points) -> Features:
        """Gets all the absolute values of the features passed in"""
        features = self._featureCreatorBase.get_features(points)
        absFeatures = Features()
        for featureVal in features:
            absFeatures.add_feature_val(abs(featureVal))

        return absFeatures

    def __str__(self) -> str:
        """This is a feature for the absolute value of another feature"""
        return "ABS:" + str(self._featureCreatorBase)