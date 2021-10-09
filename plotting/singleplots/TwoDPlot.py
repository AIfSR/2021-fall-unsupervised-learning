from plotting.singleplots.SinglePlotBase import SinglePlotBase
from features.Features import Features

class TwoDPlot (SinglePlotBase):

    def __init__(self, xFeatures:Features, yFeatures:Features) -> None:
        """Creates an instance of TwoDPlot. This class takes two features and 
        creates a two dimensional plot comparing them to each other"""
        super().__init__()
        self._xFeatures = xFeatures
        self._yFeatures = yFeatures

    # TODO This returning an object is wrong, we need to figure out what is 
    # returned here so that compare plots can create a larger image comparing 
    # all the plots 
    def getPlot(self) -> object:
        """Creates a two dimensional plot plotting two features against one a
        nother"""