from abc import ABC, abstractmethod
from typing import List, Tuple

from features.Features import Features
from tckfilereader.Points import Points

class ComparePlotsBase (ABC):

    @abstractmethod
    def display_plots(self, plotFeatures:List[Tuple[Features, Features]], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all the plots"""
        pass