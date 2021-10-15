from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features

class TFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the T coordinates of the points"""

    def get_features(self) -> Features:
        """Gets all the T values as features"""
        self._features = Features()
        for point in self._points:
            self._features.add_feature_val(point.get_t())

        return self._features