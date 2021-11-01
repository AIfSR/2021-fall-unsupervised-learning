

from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class MarkWhenFeatureValuesChange (FeatureCreatorBase):
    """Creates a feature where each value of 1 is when the value of a feature is 
    not the same as the value before it"""
    def __init__(self, origFeatureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._origFeatureCreator = origFeatureCreator

    def get_features(self, points:Points) -> Features:
        """Gets all the points where the feature changes values"""
        origFeatures = self._origFeatureCreator.get_features(points)
        features = Features()
        prevVal = origFeatures[0]
        for i in range(1, len(origFeatures)):
            currentVal = origFeatures[i]
            if currentVal == prevVal:
                features.add_feature_val(1.0)
            else:
                features.add_feature_val(0.0)
            prevVal = currentVal

        return features

    def __str__(self) -> str:
        """This is a feature for changing feature values"""
        return "Changes in:" + str(self._origFeatureCreator)