from typing import List, Tuple
from features.Features import Features
from plotting.ComparePlotsBase import ComparePlotsBase
from tckfilereader.Points import Points

class TwoDComparePlots (ComparePlotsBase):

    def __init__(self) -> None:
        super().__init__()

    def display_plots(self, plotFeatures:List[Tuple[Features, Features]], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all of the plots passed in in two dimensions"""
