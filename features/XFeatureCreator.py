from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features

class XFeatureCreator (FeatureCreatorBase):

    def get_features(self) -> Features:
        """Gets all the X values as features"""
        self._features = Features()
        for point in self._points:
            self._features.add_feature_val(point.get_x())

        return self._features