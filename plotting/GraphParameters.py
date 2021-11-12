from __future__ import annotations

from features.FeatureCreatorBase import FeatureCreatorBase
from featuretosingleval.AverageOfFeature import AverageOfFeature
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase



class GraphParameters:
    """This is just a data class that holds all of the parameters of a two dimensional graph"""

    def __init__(self, xFeatureCreator:FeatureCreatorBase, yFeatureCreator:FeatureCreatorBase=None, xLabel:str=None, yLabel:str=None, featuresToSingleVal:FeatureToSingleValBase=None) -> None:
        self.xFeatureCreator = xFeatureCreator
        self.yFeatureCreator = yFeatureCreator
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.featuresToSingleVal = featuresToSingleVal or AverageOfFeature()

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