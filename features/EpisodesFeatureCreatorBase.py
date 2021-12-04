from xlsxfilereader.Episodes import Episodes
from abc import ABC, abstractmethod
from features.Features import Features

class EpisodesFeatureCreatorBase (ABC):

    @abstractmethod
    def get_features(self, episodes:Episodes) -> Features:
        """Creates and gets the features"""
        pass
