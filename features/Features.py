from __future__  import annotations
from typing import Generator

class Features:
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

    def __eq__(self, o: Features) -> bool:
        """Checks that the values of two features are equal"""
        if not isinstance(o, Features):
            return False

        if not len(self) == len(o):
            return False
        
        for val1, val2 in zip(self, o):
            if abs(val1 - val2) > 1e-6:
                return False
        
        return True

    def __len__(self) -> int:
        """Gets the length of this feature"""
        return len(self._featuresList)

    def __str__(self):
        """Gets the string representation of this feature"""
        result = ""
        for val in self._featuresList:
            result += str(val)
            result += ", "
        return result

    def __max__(self):
        """Gets the maximium falue of this feature"""
        return max(self._featuresList)

    def to_list(self):
        """Gets the list version of this feature"""
        return self._featuresList

    def __getitem__(self, index:int) -> float:
        """Gets the FeatureValue at the specified index"""
        return self._featuresList[index]

    def __repr__(self) -> str:
        """Gets the string representation of this feature"""
        return str(self._featuresList)