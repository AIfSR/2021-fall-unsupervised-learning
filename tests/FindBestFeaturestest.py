import unittest
import FindBestFeatures
from FindBestFeatures import LabeledVector
import numpy as np

class FindBestFeaturesTest (unittest.TestCase):
    def test_5(self):
        self.assertEquals(5, 5)

    def test_contents_of_lists_the_same(self):
        lst1 = [
            LabeledVector("M0", np.array([1,2,3])),
            LabeledVector("M2", np.array([4,5,6])),
            LabeledVector("M3", np.array([7,8,9])),
        ]

        lst2 = [
            LabeledVector("M2", np.array([4,5,6])),
            LabeledVector("M3", np.array([7,8,9])),
            LabeledVector("M0", np.array([1,2,3])),
        ]

        self.assertTrue(FindBestFeatures.contents_of_lists_the_same(lst1, lst2))
