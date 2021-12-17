from typing import Iterable
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class EliminatePointsOutsideRangeFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that eliminates the features outside of a certain range"""

    def __init__(self, rangeMin:float, rangeMax:float, featureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._rangeMin = rangeMin
        self._rangeMax = rangeMax
        self._featureCreator = featureCreator

    def get_features(self, iterable:Iterable) -> Features:
        """Gets all the values within the range specified"""
        origFeatures = self._featureCreator.get_features(iterable)
        features = Features()
        count = 1
        for featureVal in origFeatures:
            if(count / len(origFeatures) <= self._rangeMax and count / len(origFeatures) >= self._rangeMin):
                features.add_feature_val(featureVal)
            
            count+= 1

        return features

    def __str__(self) -> str:
        """This is a feature for eliminating a range of values"""
        return str(self._featureCreator) + " Kept: " + str(self._rangeMin) + "-" + str(self._rangeMax)