from features.EpisodesFeatureCreatorBase import EpisodesFeatureCreatorBase
from features.Features import Features
from xlsxfilereader.Episodes import Episodes

class PercentageFeatureCreator (EpisodesFeatureCreatorBase):
    """Creates a Feature that takes the percentage of a type of episode"""

    def __init__(self,type:str):
        self.type = type

    def get_features(self, episodes:Episodes) -> Features:
        """Gets percentage of a type of episode given episodes"""
        features = Features()
        total_duration = episodes.episodesList[-1].get_occ() + episodes.episodesList[-1].get_duration()
        time = 0
        for episode in episodes:
            if episode.get_type() == self.type:
                time = time + episode.get_duration()
        percentage = time/total_duration
        features.add_feature_val(percentage)
        return features

    def __str__(self) -> str:
        """This is a feature for Percentage values"""
        return "Percentage of " + self.type

