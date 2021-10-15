

from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.TFeatureCreator import TFeatureCreator
from tckfilereader.Points import Points


class RateOfChangeFeatureCreator (FeatureCreatorBase):
    """Takes a feature and finds the rate of change over all of the values"""

    def __init__(self, points: Points, featureCreator:FeatureCreatorBase) -> None:
        super().__init__(points)
        self._featureCreator = featureCreator

    def get_features(self) -> Features:
        """Gets the rate of change of all the values in the feature created"""
        self._features = Features()

        timeFeature = TFeatureCreator(self._points).get_features()
        otherFeature = self._featureCreator.get_features()
        firstVal = True

        for val, time in zip(otherFeature, timeFeature):
            if firstVal:
                self._features.add_feature_val(0.0)
                firstVal = False
            else:
                valChange = val - prevVal
                tChange = time - prevTime
                self._features.add_feature_val(valChange / tChange)
            prevVal = val
            prevTime = time
        return self._features