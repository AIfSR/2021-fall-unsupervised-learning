from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features

class YFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the Y coordinates of the points"""

    def get_features(self) -> Features:
        """Gets all the Y values as features"""
        self._features = Features()
        for point in self._points:
            self._features.add_feature_val(point.get_y())

        return self._features