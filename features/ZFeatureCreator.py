from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features

class ZFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the Z coordinates of the points"""

    def get_features(self) -> Features:
        """Gets all the Z values as features"""
        self._features = Features()
        for point in self._points:
            self._features.add_feature_val(point.get_z())

        return self._features