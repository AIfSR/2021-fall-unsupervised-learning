from abc import ABC, abstractmethod
from typing import List
from plotting.singleplots.SinglePlotBase import SinglePlotBase

class ComparePlotsBase (ABC):

    @abstractmethod
    def display_plots(self) -> None:
        """Displays all the plots"""
        pass