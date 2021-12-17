

from typing import Iterable
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class DeltaFromStartFeatureCreator (FeatureCreatorBase):

    def __init__(self, featureCreator:FeatureCreatorBase) -> None:
        """Creates the DeltaFromStartFeatureCreator object with the 
        featureCreator that's features will be relative to the starting value"""
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, iterable:Iterable) -> Features:
        """Creates the features from the feature creator and gets eachs feature 
        value's delta from the start value."""
        origFeatures = self._featureCreator.get_features(iterable)
        features = Features()
        start = 0
        assignedStart = False
        for val in origFeatures:
            if not assignedStart:
                start = val
                assignedStart = True
            features.add_feature_val(val - start)
        return features

    def __str__(self) -> str:
        """String representation of the DeltaFromStartFeatureCreator class"""
        return "DfS:" + str(self._featureCreator)