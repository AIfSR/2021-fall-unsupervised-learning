from features.EpisodesFeatureCreatorBase import EpisodesFeatureCreatorBase
from features.Features import Features
from xlsxfilereader.Episodes import Episodes

class EpisodesABSFeatureCreator (EpisodesFeatureCreatorBase):
    """Creates a Feature that is just the absolute value of the feature creator 
    passed in"""
    def __init__(self, EpisodesFeatureCreatorBase:EpisodesFeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreatorBase = EpisodesFeatureCreatorBase

    def get_features(self, episodes:Episodes) -> Features:
        """Gets all the absolute values of the features passed in"""
        features = self._featureCreatorBase.get_features(episodes)
        absFeatures = Features()
        for featureVal in features:
            absFeatures.add_feature_val(abs(featureVal))

        return absFeatures

    def __str__(self) -> str:
        """This is a feature for the absolute value of another feature"""
        return "ABS:" + str(self._featureCreatorBase)
