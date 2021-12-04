from abc import ABC, abstractmethod
from typing import List, Tuple

from features.Features import Features
from plotting.GraphParameters import GraphParameters
from xlsxfilereader.Episodes import Episodes


class ComparePlotsBase (ABC):

    @abstractmethod
    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Episodes]]]) -> None:
        """Displays all the plots"""
        pass
