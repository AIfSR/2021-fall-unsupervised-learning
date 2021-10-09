from abc import ABC, abstractmethod
from typing import List
from plotting.singleplots.SinglePlotBase import SinglePlotBase

class ComparePlotsBase (ABC):

    def __init__(self, singlePlots:List[SinglePlotBase]) -> None:
        """Creates an instance of ComparePlots that takes in a list of 
        singlePlots to compare to one another."""
        super().__init__()
        self._singlePlotsList = singlePlots

    # TODO This returning an object is wrong. Once we know how to return plots 
    # that is what the return type here should be
    @abstractmethod
    def get_plot_comparison(self) -> object:
        """Gets a plot that compares all of the plots passed in."""
        pass