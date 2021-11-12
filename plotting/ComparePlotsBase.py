from abc import ABC, abstractmethod
from typing import List, Tuple

from features.Features import Features
from plotting.GraphParameters import GraphParameters
from tckfilereader.Points import Points


class ComparePlotsBase (ABC):

    @abstractmethod
    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        """Displays all the plots"""
        pass
