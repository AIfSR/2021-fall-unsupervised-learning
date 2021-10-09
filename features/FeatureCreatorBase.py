from tckfilereader.Points import Points
from abc import ABC, abstractmethod
from features.Features import Features

class FeatureCreatorBase (ABC):

    def __init__(self, points:Points) -> None:
        """Saves points in a member variable when creating FeatureBase 
        instance"""
        self._points = Points

    @abstractmethod
    def getFeatures(self) -> Features:
        """Creates and gets the features"""
    