from typing import List
from xlsxfilereader.Episode import Episode

class EpisodesIterator:
    """Iterator class """
    def __init__(self, episodes):
        self._episodes = episodes
        self._index = 0

    def __next__(self):
        """Returns the next value from Episodes object's lists"""
        if self._index < (len(self._episodes.episodesList)):
            result = self._episodes.episodesList[self._index]
            self._index += 1
            return result
        raise StopIteration

class Episodes:
    def __init__(self, episodesList:List[Episode]=None) -> None:
        """A Episodes class stores all the episodes generated from a tck file"""
        self.episodesList = episodesList or []
        pass
    
    def addEpisode(self, episode:Episode) -> None:
        """Adds the Episode to the list of episodes"""
        self.episodesList.append(episode)

    def __str__(self) -> str:
        """displays array in a string"""
        _result = ""
        for counter in range(len(self.episodesList)-1):
            _result += "Episode(%s,%s,%s,%s)," % (self.episodesList[counter].type,self.episodesList[counter].n, self.episodesList[counter].occ, self.episodesList[counter].duration)
        _result += "Episode(%s,%s,%s,%s)" % (self.episodesList[len(self.episodesList)-1].type,self.episodesList[len(self.episodesList)-1].n, self.episodesList[len(self.episodesList)-1].occ, self.episodesList[len(self.episodesList)-1].duration)
        return _result

    def __iter__(self):
        """Returns the Iterator object"""
        return EpisodesIterator(self)

    def __eq__(self, other):
        return self.episodesList == other.episodesList

    def __getitem__(self, index:int) -> Episode:
        """Gets the Episode at the specified index"""
        return self.episodesList[index]

    def __len__(self) -> int:
        """Gets the number of episodes in this Episodes object"""
        return len(self.episodesList)

    def sort(self):
        self.episodesList.sort()




