import unittest

from features.Features import Features
from plotting.singlepointcomparetrajectories.SinglePointCompareTrajectories import SinglePointCompareTrajectories
from plotting.singlepointcomparetrajectories.LineFeatureCreator import LineFeatureCreator
from featuretosingleval.AverageOfFeature import AverageOfFeature
from tckfilereader.Point import Point
from tckfilereader.Points import Points

class SinglePointCompareTrajectoriesTest (unittest.TestCase):

    def test_calculate_hist_height(self) -> None:
        """Tests calculating the height for each histogram"""

        solution = (1.0 - (SinglePointCompareTrajectories.BOTTOM * 2 + SinglePointCompareTrajectories.HEIGHT + 2 * SinglePointCompareTrajectories.SPACING)) / 2
        singlePointCompareTrajectories = SinglePointCompareTrajectories(None)
        self.assertAlmostEquals(solution, singlePointCompareTrajectories._calculate_hist_height(2))


