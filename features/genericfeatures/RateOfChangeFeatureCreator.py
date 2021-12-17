

from typing import Iterable
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.pointsfeatures.TFeatureCreator import TFeatureCreator
from tckfilereader.Points import Points


class RateOfChangeFeatureCreator (FeatureCreatorBase):
    """Takes a feature and finds the rate of change over all of the values"""

    def __init__(self, featureCreator:FeatureCreatorBase, timeFeatureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator
        self._timeFeatureCreator = timeFeatureCreator

    def get_features(self, iterable:Iterable) -> Features:
        """Gets the rate of change of all the values in the feature created"""
        features = Features()

        timeFeature = self._timeFeatureCreator.get_features(iterable)
        otherFeature = self._featureCreator.get_features(iterable)
        firstVal = True

        for val, time in zip(otherFeature, timeFeature):
            if firstVal:
                firstVal = False
            else:
                valChange = val - prevVal
                tChange = time - prevTime
                features.add_feature_val(valChange / tChange)
            prevVal = val
            prevTime = time
        return features

    def __str__(self) -> str:
        """This is a feature for the Rate of change of another feature"""
        if not isinstance(self._featureCreator, RateOfChangeFeatureCreator):
            return "RoC:" + str(self._featureCreator)
        
        featureString = str(self._featureCreator)
        stringWithoutRoc = featureString[3:]
        if stringWithoutRoc[0] == ":":
            return "RoC^2" + stringWithoutRoc
        
        for i in range(1, len(stringWithoutRoc)):
            if stringWithoutRoc[i] == ":":
                break
        number = stringWithoutRoc[1:i]
        return "RoC^" + str(int(number) + 1) + stringWithoutRoc[i:]
