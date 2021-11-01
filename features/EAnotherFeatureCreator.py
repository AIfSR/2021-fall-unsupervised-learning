from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points
import math

class EAnotherFeatureCreator (FeatureCreatorBase):
    """Creates a feature that just raises e to the absolute values of another feature"""
    def __init__(self, origFeatureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._origFeatureCreator = origFeatureCreator

    def get_features(self, points:Points) -> Features:
        """Gets e raied to all the features in the original feature creator"""
        origFeatures = self._origFeatureCreator.get_features(points)
        features = Features()
        for featureVal in origFeatures:
            features.add_feature_val(math.e**(abs(featureVal)))
        return features

    def __str__(self) -> str:
        """This is a feature for e-ing another feature"""
        return "E^: " + str(self._origFeatureCreator)