import unittest
from features.Features import Features

class FeaturesTest (unittest.TestCase):

    def test_add_feature(self):
        """Tests the add_feature_val method in Feature"""
        feature = Features()
        solution = [1,2,3]
        feature.add_feature_val(solution[0])
        feature.add_feature_val(solution[1])
        feature.add_feature_val(solution[2])
        
        for val, solutionVal in zip(feature, solution):
            self.assertEquals(val, solutionVal)

    def test_equals(self):
        """Tests the equals operator for Feature instances"""
        feature1 = Features()
        feature2 = Features()
        feature3 = Features()
        feature4 = Features()

        feature1.add_feature_val(1)
        feature1.add_feature_val(2)
        
        feature2.add_feature_val(1)
        feature2.add_feature_val(2)
        
        feature3.add_feature_val(3)
        feature3.add_feature_val(2)
        
        feature4.add_feature_val(1)
        feature4.add_feature_val(2)
        feature4.add_feature_val(3)

        self.assertTrue(feature1 == feature2)
        self.assertFalse(feature1 == feature3)
        self.assertFalse(feature1 == feature4)

    def test_length(self):
        """Tests the len() operator on a Feature instance"""
        feature = Features()
        self.assertEquals(len(feature), 0)
        feature.add_feature_val(1)
        feature.add_feature_val(2)

        self.assertEquals(len(feature), 2)

    def test_string(self):
        """Tests the str() operator on a Feature instance"""
        feature = Features()
        solution = [1,2,3]
        feature.add_feature_val(solution[0])
        feature.add_feature_val(solution[1])
        self.assertEquals(str(feature), "1, 2, ")

    def test_max(self):
        """Tests the max() operator on a Feature instance"""
        feature = Features()
        feature.add_feature_val(1)
        feature.add_feature_val(2)
        feature.add_feature_val(8)
        feature.add_feature_val(4)
        feature.add_feature_val(-2)
        feature.add_feature_val(-100)

        self.assertEquals(max(feature), 8)
    def test_to_list(self):
        """Tests the to_list methood of a Feature"""
        solution = [1,5,6,2,5,8,9]
        feature = Features()
        for val in solution:
            feature.add_feature_val(val)
        self.assertEquals(feature.to_list(), solution)
