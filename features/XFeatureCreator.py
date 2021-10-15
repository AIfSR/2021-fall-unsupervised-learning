from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class XFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the X coordinates of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the X values as features"""
        features = Features()
        for point in points:
            features.add_feature_val(point.get_x())

        return features