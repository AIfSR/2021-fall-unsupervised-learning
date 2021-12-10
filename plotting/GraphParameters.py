from __future__ import annotations

from features.FeatureCreatorBase import FeatureCreatorBase
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase



class GraphParameters:
    """This is just a data class that holds all of the parameters of a two dimensional graph"""

    def __init__(self, xFeatureCreator:FeatureCreatorBase, yFeatureCreator:FeatureCreatorBase=None, xLabel:str=None, yLabel:str=None, featuresToSingleVal:FeatureToSingleValBase=None) -> None:
        self.featuresToSingleVal = featuresToSingleVal or AverageOfFeature()
        self.xFeatureCreator = xFeatureCreator
        self.yFeatureCreator = yFeatureCreator
        if featuresToSingleVal is not None and xFeatureCreator is not None:
            self.xLabel = str(self.featuresToSingleVal) + " " + str(self.xFeatureCreator)
        else:
            self.xLabel = xLabel
        if featuresToSingleVal is not None and yFeatureCreator is not None:
            self.yLabel = str(self.featuresToSingleVal) + " " + str(self.yFeatureCreator)
        else:
            self.yLabel = yLabel

    def __eq__(self, o: GraphParameters) -> bool:
        if not isinstance(o, GraphParameters):
            return False
        return (
            type(self.xFeatureCreator) == type(o.xFeatureCreator) and
            type(self.yFeatureCreator) == type(o.yFeatureCreator) and
            type(self.featuresToSingleVal) == type(o.featuresToSingleVal) and
            self.xLabel == o.xLabel and
            self.yLabel == o.yLabel 
        )

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.xFeatureCreator,self.yFeatureCreator,self.xLabel, self.yLabel, self.featuresToSingleVal)
