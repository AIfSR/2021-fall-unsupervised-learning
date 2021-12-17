from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class TFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that is just the T coordinates of the points"""

    def get_features(self, points: Points) -> Features:
        """Gets all the T values as features"""
        features = Features()
        for point in points:
            features.add_feature_val(point.get_t())

        return features

    def __str__(self) -> str:
        """This is a feature for T coords"""
        return "T"