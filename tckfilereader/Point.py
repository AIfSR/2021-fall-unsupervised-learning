class Point(object):
    def __init__(self, x: float, y: float, z: float, t: float) -> None:
        """Creates a point with the specified x, y, z, and t coordinates"""
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __iter__(self):
        pass

    def __str__(self) -> str:
        """Displays Point Object"""
        return "Point(%s,%s,%s,%s)" % (self.x, self.y, self.z, self.t)

    def get_x(self) -> float:
        """Defines x variables"""
        return self.x

    def get_y(self) -> float:
        """Defines y variables"""
        return self.y

    def get_z(self) -> float:
        """Defines z variables"""
        return self.z

    def get_t(self) -> float:
        """Defines t variables"""
        return self.t
