import unittest

from features.Features import Features
from plotting.SinglePointCompareTrajectories import SinglePointCompareTrajectories

class SinglePointCompareTrajectoriesTest (unittest.TestCase):

    def test_get_average_of_feature(self) -> None:
        """Tests the method that gets the average of a feature"""
        feature = Features()
        lst = [1,2,3,5,2.7,4.6,2.3]
        for val in lst:
            feature.add_feature_val(val)
        solution = sum(lst) / len(lst)
        singlePointCompareTrajectories = SinglePointCompareTrajectories()
        self.assertEquals(singlePointCompareTrajectories._get_average_of_feature(feature), solution)
