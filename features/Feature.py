from __future__  import annotations
from typing import Generator

class Feature:
    """A class to store the values for a feature of a learning algorithm"""

    def __init__(self) -> None:
        """Creates a list to internally store the features"""
        self._featuresList = []

    def add_feature_val(self, val:float) -> None:
        """Adds a value to this feature"""
        self._featuresList.append(val)

    def __iter__(self) -> Generator:
        """Creates a generator that reveals all the values in this feature"""
        for val in self._featuresList:
            yield val

    def __eq__(self, o: Feature) -> bool:
        """Checks that the values of two features are equal"""
        if not isinstance(o, Feature):
            return False

        if not len(self) == len(o):
            return False
        
        for val1, val2 in zip(self, o):
            if not val1 == val2:
                return False
        
        return True

    def __len__(self) -> int:
        """Gets the length of this feature"""
        return len(self._featuresList)