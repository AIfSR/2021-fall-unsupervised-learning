class Episode(object):
    def __init__(self, type: str, n: float, occ: float, duration: float) -> None:
        """Creates a episode with the specified x, y, z, and t coordinates"""
        self.type = str(type)
        self.n = float(n)
        self.occ = float(occ)
        self.duration = float(duration)

    def __eq__(self, other):
        return self.type == other.type and \
               self.n == other.n and \
               self.occ == other.occ and \
               self.duration == other.duration

    def __iter__(self):
        pass

    def __str__(self) -> str:
        """Displays episode Object"""
        return "Episode(%s,%s,%s,%s)" % (self.type, self.n, self.occ, self.duration)

    def get_type(self) -> float:
        """Defines x variables"""
        return self.type

    def get_n(self) -> float:
        """Defines x variables"""
        return self.n

    def get_occ(self) -> float:
        """Defines y variables"""
        return self.occ

    def get_duration(self) -> float:
        """Defines z variables"""
        return self.duration

    def __lt__(self, other):
        return (self.occ) < (other.occ)