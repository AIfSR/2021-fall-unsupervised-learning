from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class YFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the Y coordinates of the points"""

    def get_features(self, points:Points) -> Features:
        """Gets all the Y values as features"""
        features = Features()
        for point in points:
            features.add_feature_val(point.get_y())

        return features