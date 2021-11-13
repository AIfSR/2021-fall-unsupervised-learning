
from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class OutlierFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that marks whenever a point in the origianl feature 
    creator is an outlier"""

    def __init__(self, featureCreator:FeatureCreatorBase, maxAcceptableDeviations:float) -> None:
        super().__init__()
        self._featureCreator = featureCreator
        self._maxAcceptableDeviations = maxAcceptableDeviations

    def get_features(self, points:Points) -> Features:
        """Gets all the outliers as features"""

        stdDeviations = self._get_standard_deviations(points)
        features = Features()
        for deviation in stdDeviations:
            if abs(deviation) >= self._maxAcceptableDeviations:
                features.add_feature_val(1.0)
            else:
                features.add_feature_val(0.0)

        return features

    def _get_standard_deviations(self, points):
        features = self._featureCreator.get_features(points)
        avg = sum(features.to_list()) / len(features)
        stdDeviation = (sum([(feature - avg)**2 for feature in features]) / len(features))**0.5
        deviationsOfFeatureVals = []
        for featureval in features:
            deviations = (featureval - avg) / stdDeviation
            deviationsOfFeatureVals.append(deviations)
        return deviationsOfFeatureVals

    def __str__(self) -> str:
        """This is a feature for outliers"""
        return str(self._featureCreator) + " Outliers: " + str(self._maxAcceptableDeviations)