from typing import List, Tuple
from features.Features import Features
from plotting.ComparePlotsBase import ComparePlotsBase

class TwoDComparePlots (ComparePlotsBase):

    def __init__(self, plotFeatures:List[Tuple[Features, Features]]) -> None:
        super().__init__()
        self._plotFeatures = plotFeatures

    def display_plots(self) -> None:
        """Displays all of the plots passed in in two dimensions"""
