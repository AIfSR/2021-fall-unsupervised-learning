from typing import Iterable
from tckfilereader.Points import Points
from abc import ABC, abstractmethod
from features.Features import Features

class FeatureCreatorBase (ABC):

    @abstractmethod
    def get_features(self, iterable:Iterable) -> Features:
        """Creates and gets the features"""
        pass
    