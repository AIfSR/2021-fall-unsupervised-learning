

from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.TFeatureCreator import TFeatureCreator
from tckfilereader.Points import Points


class RateOfChangeFeatureCreator (FeatureCreatorBase):
    """Takes a feature and finds the rate of change over all of the values"""

    def __init__(self, featureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, points: Points) -> Features:
        """Gets the rate of change of all the values in the feature created"""
        features = Features()

        timeFeature = TFeatureCreator().get_features(points)
        otherFeature = self._featureCreator.get_features(points)
        firstVal = True

        for val, time in zip(otherFeature, timeFeature):
            if firstVal:
                features.add_feature_val(0.0)
                # this line needs to be here so that there are an equal amount 
                # of feature values as points passed in
                firstVal = False
            else:
                valChange = val - prevVal
                tChange = time - prevTime
                features.add_feature_val(valChange / tChange)
            prevVal = val
            prevTime = time
        return features

    def __str__(self) -> str:
        """This is a feature for the Rate of change of another feature"""
        if not isinstance(self._featureCreator, RateOfChangeFeatureCreator):
            return "RoC:" + str(self._featureCreator)
        
        featureString = str(self._featureCreator)
        stringWithoutRoc = featureString[3:]
        if stringWithoutRoc[0] == ":":
            return "RoC^2" + stringWithoutRoc
        
        for i in range(1, len(stringWithoutRoc)):
            if stringWithoutRoc[i] == ":":
                break
        number = stringWithoutRoc[1:i]
        return "RoC^" + str(int(number) + 1) + stringWithoutRoc[i:]