from features.FeatureCreatorBase import FeatureCreatorBase
from xlsxfilereader.Episodes import Episodes
from features.Features import Features

class LineFeatureCreator (FeatureCreatorBase):

    def __init__(self) -> None:
        super().__init__()
        self._val = 0.0

    def increment(self):
        self._val += 1

    def get_features(self, episodes:Episodes) -> Features:
        """Creates a feature with only 0s so the scatter plot is a strait line"""
        feature = Features()
        for episode in episodes:
            feature.add_feature_val(self._val)
        return feature

    def __str__(self) -> str:
        return ""
