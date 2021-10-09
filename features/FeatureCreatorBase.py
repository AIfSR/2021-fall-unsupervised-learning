from tckfilereader.Points import Points
from abc import ABC, abstractmethod
from features.Features import Features

class FeatureCreatorBase (ABC):

    def __init__(self, points:Points) -> None:
        """Saves points in a member variable when creating FeatureBase 
        instance"""
        self._points = Points
        self._features = Features()

    @abstractmethod
    def get_features(self) -> Features:
        """Creates and gets the features"""
        pass
    