from features.FeatureCreatorBase import FeatureCreatorBase
from features.Features import Features
from features.TFeatureCreator import TFeatureCreator
from tckfilereader.Points import Points
import numpy as np


class MSDFeatureCreator(FeatureCreatorBase):
    """Takes a feature and finds the rate of change over all of the values"""

    def __init__(self, featureCreator:FeatureCreatorBase) -> None:
        super().__init__()
        self._featureCreator = featureCreator

    def get_features(self, points: Points) -> Features:
        features = Features()
        timeFeature = TFeatureCreator().get_features(points)
        otherFeature = self._featureCreator.get_features(points)
        firstVal = True

        N = len(timeFeature)
        """Gets the rate of change of all the values in the feature created"""
        # MSDinX = np.array(otherFeature[0:N])
        x = otherFeature._featuresList
        DispX = np.zeros((N, N)).astype('float64')
        for k in range(1,N):
            for i in range(N - k):
                DispX[k, i] = (x[i] - x[i + k]) ** 2

        for j in range(N):
            # MSDinX[j] = np.sum(DispX[j, 0:N - j]) / (N - j)
            features.add_feature_val(np.sum(DispX[j, 0:N - j]) / (N - j))
        # features._featuresList = features._featuresList[:-2]
        return features

        # for val, time in zip(otherFeature, timeFeature):
        #     if firstVal:
        #         # features.add_feature_val(0.0)
        #         # # this line needs to be here so that there are an equal amount
        #         # # of feature values as points passed in
        #         firstVal = False
        #     else:
        #         valChange = val - prevVal
        #         tChange = time - prevTime
        #         features.add_feature_val((valChange ** 2) / tChange)
        #     prevVal = val
        #     prevTime = time
        # return features

    def __str__(self) -> str:
        """This is a feature for the Mean Squared Displacement of another feature"""
        if not isinstance(self._featureCreator, MSDFeatureCreator):
            return "MSD:" + str(self._featureCreator)

        featureString = str(self._featureCreator)
        stringWithoutMSD = featureString[3:]
        if stringWithoutMSD[0] == ":":
            return "MSD^2" + stringWithoutMSD

        for i in range(1, len(stringWithoutMSD)):
            if stringWithoutMSD[i] == ":":
                break
        number = stringWithoutMSD[1:i]
        return "MSD^" + str(int(number) + 1) + stringWithoutMSD[i:]
