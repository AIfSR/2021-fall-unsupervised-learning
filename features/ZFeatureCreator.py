from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class ZFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the Z coordinates of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the Z values as features"""
        features = Features()
        for point in points:
            features.add_feature_val(point.get_z())

        return features