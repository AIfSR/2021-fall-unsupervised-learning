

from typing import List, Tuple
from features.Features import Features
from featuretosingleval.FeatureToSingleValBase import FeatureToSingleValBase
from plotting.ComparePlotsBase import ComparePlotsBase
from plotting.GraphParameters import GraphParameters
from tckfilereader.Points import Points


class SinglePoint1DCompareTrajectories (ComparePlotsBase):

    def __init__(self) -> None:
        super().__init__()

    def display_plots(self, graphParameters:List[GraphParameters], categories:List[Tuple[str,List[Points]]]) -> None:
        pass