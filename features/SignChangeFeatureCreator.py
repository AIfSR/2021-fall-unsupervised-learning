from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from tckfilereader.Points import Points

class SignChangeFeatureCreator (FeatureCreatorBase):
    """Creates a Feature that marks whenever another feature changes sign"""
    def __init__(self, featureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, points:Points) -> Features:
        """Gets all the sign changes as features"""
        features = self._featureCreator.get_features(points)
        signChangeFeatures = Features()
        prevVal = None
        for featureVal in features:
            if prevVal == None:
                signChangeFeatures.add_feature_val(0.0)
            elif (featureVal >= 0.0 and prevVal >= 0.0) or (featureVal < 0.0 and prevVal < 0.0):
                signChangeFeatures.add_feature_val(0.0)
            else:
                signChangeFeatures.add_feature_val(1.0)
            prevVal = featureVal

        return signChangeFeatures

    def __str__(self) -> str:
        """This is a feature for sign changes"""
        return "SignChange:" + str(self._featureCreator)