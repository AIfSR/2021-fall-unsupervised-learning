from features.EpisodesFeatureCreatorBase import EpisodesFeatureCreatorBase
from features.Features import Features
from xlsxfilereader.Episodes import Episodes

class DurationFeatureCreator(EpisodesFeatureCreatorBase):
    """Creates a Feature that is just the Duration values of episodes"""

    def get_features(self, episodes:Episodes) -> Features:
        """Gets all the Duration values as features"""
        features = Features()
        for episode in episodes:
            features.add_feature_val(episode.get_duration())

        return features

    def __str__(self) -> str:
        """This is a feature for Duration values"""
        return "Duration"
