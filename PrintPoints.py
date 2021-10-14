from tckfilereader.TCKFileReader import TCKFileReader
from tckfilereader.Points import Points
from tckfilereader.Point import Point

m0FilePaths = [
    "data/0_24h/M0/2020-12-17_10-20-56,683_.tck",
    "data/0_24h/M0/2020-12-17_13-02-13,789_.tck",
    "data/0_24h/M0/2020-12-17_11-07-35,778_.tck",

    "data/0_4h/M0/2020-08-05_16-45-01,168_.tck",
    "data/0_4h/M0/2020-08-05_17-21-46,888_.tck",
    "data/0_4h/M0/2020-08-05_18-11-44,490_.tck",
    "data/0_4h/M0/2020-12-02_14-49-41,154_.tck",
    "data/0_4h/M0/2020-12-02_15-58-23,371_.tck",
    "data/0_4h/M0/2020-12-02_16-41-18,342_.tck",

    "data/24h_24h/M0/2020-10-23_18-48-03,252_.tck",
    "data/24h_24h/M0/2020-10-23_19-16-43,054_.tck",
    "data/24h_24h/M0/2020-11-13_09-56-18,599_.tck",

    "data/24h_4h/M0/2020-09-24_15-31-22,100_.tck",
    "data/24h_4h/M0/2020-09-24_17-00-57,463_.tck",
    "data/24h_4h/M0/2020-09-24_16-16-27,474_.tck",
    "data/24h_4h/M0/2020-11-12_16-12-49,016_.tck",
]

m1FilePaths = [
    "data/0_24h/M1/2020-08-06_16-00-42,831_.tck",
    "data/0_24h/M1/2020-08-06_17-07-43,536_.tck",
    "data/0_24h/M1/2020-08-06_16-28-09,982_.tck",
    "data/0_24h/M1/2020-08-06_17-44-38,166_.tck",

    "data/0_4h/M1/2020-08-05_18-51-50,514_.tck",
    "data/0_4h/M1/2020-08-05_19-18-08,801_.tck",
    "data/0_4h/M1/2020-08-05_20-12-39,857_.tck",
    "data/0_4h/M1/2020-08-05_20-44-17,610_.tck",
    "data/0_4h/M1/2020-08-05_21-48-48,900_.tck",
    "data/0_4h/M1/2020-08-05_22-33-50,826_.tck",

    "data/24h_24h/M1/2020-08-27_15-47-02,026_.tck",
    "data/24h_24h/M1/2020-08-27_17-07-16,954_.tck",
    "data/24h_24h/M1/2020-08-27_18-19-30,067_.tck",
    "data/24h_24h/M1/2020-11-05_18-18-55,017_.tck",
    "data/24h_24h/M1/2020-11-13_14-34-21,558_.tck",

    "data/24h_4h/M1/2020-11-12_20-01-59,972_.tck",
    "data/24h_4h/M1/2020-11-12_20-51-02,405_.tck",
    "data/24h_4h/M1/2020-11-12_21-23-17,103_.tck",
]

m2FilePaths = [
    "data/0_24h/M2/2020-12-03_16-27-23,050_.tck",
    "data/0_24h/M2/2020-12-03_16-55-34,539_.tck",
    "data/0_24h/M2/2020-12-03_20-03-25,144_.tck",
    "data/0_24h/M2/2020-12-17_15-12-12,655_.tck",
    "data/0_24h/M2/2020-12-17_16-12-44,462_.tck",
    "data/0_24h/M2/2020-12-17_16-52-18,642_.tck",

    "data/0_4h/M2/2020-12-02_17-08-21,199_.tck",
    "data/0_4h/M2/2020-12-02_17-50-33,515_.tck",
    "data/0_4h/M2/2020-12-02_18-56-04,307_.tck",
    "data/0_4h/M2/2020-12-16_20-05-05,492_.tck",
    "data/0_4h/M2/2020-12-16_21-53-37,370_.tck",
    "data/0_4h/M2/2020-12-16_22-54-31,916_.tck",

    "data/24h_24h/M2/2020-12-11_18-08-48,051_.tck",
    "data/24h_24h/M2/2020-12-11_18-41-12,360_.tck",
    "data/24h_24h/M2/2020-12-11_19-15-07,942_.tck",

    "data/24h_4h/M2/2020-12-10_19-19-16,045_.tck",
    "data/24h_4h/M2/2020-12-10_19-54-26,923_.tck",
    "data/24h_4h/M2/2020-12-10_21-40-27,025_.tck",
    "data/24h_4h/M2/2020-12-10_22-37-02,878_.tck",
]

dest = "/Users/seandoyle/NYU/classes/AIfSR"

if __name__ == "__main__":
    print("Starting")
    tckFileReader = TCKFileReader()
    
    def placeCoordsInTextFile(files):
        for file in files:
            txtFileName = file[:-3] + "txt"
            destFullPath = dest + "/" + txtFileName
            newFileObject = open(destFullPath, "w+")
            points = tckFileReader.get_points(file)

            xList = []
            yList = []
            zList = []
            tList = []

            for point in points:
                xList.append(point.get_x())
                yList.append(point.get_y())
                zList.append(point.get_z())
                tList.append(point.get_t())
            
            newFileObject.write("X: [\n")
            for val in xList:
                newFileObject.write(str(val) + ",\n")
            newFileObject.write("]\n")
            
            newFileObject.write("Y: [\n")
            for val in yList:
                newFileObject.write(str(val) + ",\n")
            newFileObject.write("]\n")
           
            newFileObject.write("Z: [\n")
            for val in zList:
                newFileObject.write(str(val) + ",\n")
            newFileObject.write("]\n")
            
            newFileObject.write("T: [\n")
            for val in tList:
                newFileObject.write(str(val) + ",\n")
            newFileObject.write("]")
            
            newFileObject.close()
            
    placeCoordsInTextFile(m0FilePaths)
    placeCoordsInTextFile(m1FilePaths)
    placeCoordsInTextFile(m2FilePaths)
    