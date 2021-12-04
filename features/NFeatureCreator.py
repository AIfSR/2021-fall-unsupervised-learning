from features.EpisodesFeatureCreatorBase import EpisodesFeatureCreatorBase
from features.Features import Features
from xlsxfilereader.Episodes import Episodes

class NFeatureCreator (EpisodesFeatureCreatorBase):
    """Creates a Feature that is just the N values of episodes"""

    def get_features(self, episodes:Episodes) -> Features:
        """Gets all the N values as features"""
        features = Features()
        for episode in episodes:
            features.add_feature_val(episode.get_n())

        return features

    def __str__(self) -> str:
        """This is a feature for N values"""
        return "N"
