from abc import ABC, abstractmethod

class SinglePlotBase (ABC):

    # TODO This returning an object is wrong, we need to figure out what is 
    # returned here so that compare plots can create a larger image comparing 
    # all the plots 
    @abstractmethod
    def getPlot(self) -> object:
        """Gets the plot for this SinglePlot instance"""
        pass