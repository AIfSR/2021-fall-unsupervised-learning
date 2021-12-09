from features.FeatureCreatorBase import FeatureCreatorBase
from tckfilereader.Points import Points
from features.Features import Features

class LineFeatureCreator (FeatureCreatorBase):

    def __init__(self) -> None:
        super().__init__()
        self._val = 0.0

    def increment(self):
        self._val += 1

    def get_features(self, points:Points) -> Features:
        """Creates a feature with only 0s so the scatter plot is a strait line"""
        feature = Features()
        for point in points:
            feature.add_feature_val(self._val)
        return feature

    def __str__(self) -> str:
        return ""