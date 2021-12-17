from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from xlsxfilereader.Episodes import Episodes

class TypeFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the Type values of episodes"""

    def get_features(self, episodes:Episodes) -> Features:
        """Gets all the Type values as features"""
        features = Features()
        for episode in episodes:
            features.add_feature_val(episode.get_type())

        return features

    def __str__(self) -> str:
        """This is a feature for Type values"""
        return "Type"
