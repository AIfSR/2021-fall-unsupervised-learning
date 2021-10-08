from tckfilereader.Points import Points

class TCKFileReader:
    
    def get_points(self, path_to_tck_file:str) -> Points:
        """Gets all of the points from the specified TCK file."""