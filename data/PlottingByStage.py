from typing import List, Tuple
# from features.Features import Features
from tckreader import convert_file
from tckreader import user_info
from Points import Points
from Point import Point
import matplotlib.pyplot as plt
import numpy
import math

class PlottingOrganizedByStage():

    def __init__(self, stage) -> None:
        super().__init__()
        self._stage = stage

    def display_plots_XT(self) -> None:
        """Displays all of the plots passed in two dimensions"""
        #0_4h
        zero_four_file_M0_names = ["2020-08-05_16-45-01,168_.tck", "2020-08-05_17-21-46,888_.tck", "2020-08-05_18-11-44,490_.tck", "2020-12-02_14-49-41,154_.tck", "2020-12-02_15-58-23,371_.tck", "2020-12-02_16-41-18,342_.tck"]
        zero_four_file_M1_names = ["2020-08-05_18-51-50,514_.tck", "2020-08-05_19-18-08,801_.tck", "2020-08-05_20-12-39,857_.tck", "2020-08-05_20-44-17,610_.tck", "2020-08-05_21-48-48,900_.tck", "2020-08-05_22-33-50,826_.tck"]
        zero_four_file_M2_names = ["2020-12-02_17-08-21,199_.tck", "2020-12-02_17-50-33,515_.tck", "2020-12-02_18-56-04,307_.tck", "2020-12-16_20-05-05,492_.tck", "2020-12-16_21-53-37,370_.tck", "2020-12-16_22-54-31,916_.tck"]
        zero_four_files = [zero_four_file_M0_names,zero_four_file_M1_names,zero_four_file_M2_names]
#0_4    #0_4h
        # zero_twenty_four_file_names = ["2020-12-17_10-20-56,683_.tck","2020-12-17_11-07-35,778_.tck","2020-12-17_13-02-13,789_.tck"]
        # twenty_four_four_file_names = ["2020-12-02_17-08-21,199_.tck","2020-12-02_17-50-33,515_.tck","2020-12-02_18-56-04,307_.tck","2020-12-16_20-05-05,492_.tck","2020-12-16_21-53-37,370_.tck","2020-12-16_22-54-31,916_.tck"]
        # twenty_four_twenty_four_file_names = ["2020-09-24_15-31-22,100_.tck","2020-09-24_16-16-27,474_.tck","2020-09-24_17-00-57,463_.tck","2020-11-12_16-12-49,016_.tck"]
        biggest_size = 0;
        for i in zero_four_files:
            if len(i) > biggest_size:
                biggest_size = len(i)
        figure, axis = plt.subplots(3, biggest_size)
        M0_points = []
        M1_points = []
        M2_points = []
        for i in range(len(zero_four_files)):
            for j in range(len(zero_four_files[i])):
                if i == 0:
                    points = convert_file(zero_four_files[i][j])
                    M0_points.append(points)
                elif i == 1:
                    points = convert_file(zero_four_files[i][j])
                    M1_points.append(points)
                elif i == 2:
                    points = convert_file(zero_four_files[i][j])
                    M2_points.append(points)
        MO_X = []
        for x in M0_points:
            for y in x:
                individual_x = []
                individual_x.append(y.get_x)
            MO_X.append(individual_x)

        # for p2 in zero_twenty_four_file_names:
        #     X2.append(p2.get_x)
        #     T2.append(p2.get_t)
        # for p3 in twenty_four_four_file_names:
        #     X3.append(p3.get_x)
        #     T3.append(p3.get_t)
        # for p4 in twenty_four_twenty_four_file_names:
        #     X4.append(p4.get_x)
        #     T4.append(p4.get_t)
        # # For Sine Function
        # axis[0, 0].plot(X1, T1)
        # axis[0, 0].set_title("Sine Function")
        #
        # # For Cosine Function
        # axis[0, 1].plot(X2, T2)
        # axis[0, 1].set_title("Cosine Function")
        #
        # # For Tangent Function
        # axis[0, 2].plot(X3, T3)
        # axis[0, 2].set_title("Tangent Function")
        #
        # # For Tanh Function
        # axis[0, 3].plot(X4, T4)
        # axis[0, 3].set_title("Tanh Function")
        #
        # # Combine all the operations and display
        # plt.show()

if __name__ == "__main__":
    timing = input("Input timing: ")
    additional_path = "Tracking_macrophages_biosetup/"+timing+"/"
    zero_four_file_M0_names = ["2020-08-05_16-45-01,168_.tck", "2020-08-05_17-21-46,888_.tck", "2020-08-05_18-11-44,490_.tck", "2020-12-02_14-49-41,154_.tck", "2020-12-02_15-58-23,371_.tck", "2020-12-02_16-41-18,342_.tck"]
    zero_four_file_M1_names = ["2020-08-05_18-51-50,514_.tck", "2020-08-05_19-18-08,801_.tck", "2020-08-05_20-12-39,857_.tck", "2020-08-05_20-44-17,610_.tck", "2020-08-05_21-48-48,900_.tck", "2020-08-05_22-33-50,826_.tck"]
    zero_four_file_M2_names = ["2020-12-02_17-08-21,199_.tck", "2020-12-02_17-50-33,515_.tck", "2020-12-02_18-56-04,307_.tck", "2020-12-16_20-05-05,492_.tck", "2020-12-16_21-53-37,370_.tck", "2020-12-16_22-54-31,916_.tck"]
    zero_four_files = [zero_four_file_M0_names,zero_four_file_M1_names,zero_four_file_M2_names]
    points = convert_file(additional_path+ "M0/"+"2020-08-05_16-45-01,168_.tck")
    figure, axis = plt.subplots(6, 6)
#0_4
    # zero_twenty_four_file_names = ["2020-12-17_10-20-56,683_.tck","2020-12-17_11-07-35,778_.tck","2020-12-17_13-02-13,789_.tck"]
    # twenty_four_four_file_names = ["2020-12-02_17-08-21,199_.tck","2020-12-02_17-50-33,515_.tck","2020-12-02_18-56-04,307_.tck","2020-12-16_20-05-05,492_.tck","2020-12-16_21-53-37,370_.tck","2020-12-16_22-54-31,916_.tck"]
    # twenty_four_twenty_four_file_names = ["2020-09-24_15-31-22,100_.tck","2020-09-24_16-16-27,474_.tck","2020-09-24_17-00-57,463_.tck","2020-11-12_16-12-49,016_.tck"]
    # biggest_size = 0;
    # for i in zero_four_files:
    #     if len(i) > biggest_size:
    #         biggest_size = len(i)
    # figure, axis = plt.subplots(biggest_size, biggest_size)
    # M0_points = []
    # M1_points = []
    # M2_points = []
    # for i in range(len(zero_four_files)):
    #     for j in range(len(zero_four_files[i])):
    #         if i == 0:
    #             points = convert_file(additional_path+ "M0/"+zero_four_files[i][j])
    #             M0_points.append(points)
    #         elif i == 1:
    #             points = convert_file(additional_path+ "M1/"+zero_four_files[i][j])
    #             M1_points.append(points)
    #         elif i == 2:
    #             points = convert_file(additional_path+ "M2/"+zero_four_files[i][j])
    #             M2_points.append(points)
    # M0_X = []
    # M0_T = []
    # for x in M0_points:
    #     for y in x:
    #         x_values = []
    #         x_values.append(y.get_x)
    #         t_values = []
    #         t_values.append(y.get_t)
    #     x_values_arr = numpy.array(x_values)
    #     t_values_arr = numpy.array(t_values)
    #     M0_X.append(x_values_arr)
    #     M0_T.append(x_values_arr)
    # M0_X_arr = numpy.array(M0_X)
    # M0_T_arr = numpy.array(M0_T)
    # for i in range(len(M0_X_arr)):
    #     axis[i,0].plot(M0_X_arr[i], M0_T_arr[i])

    # M1_X = []
    # M1_T = []
    # for x in M1_points:
    #     for y in x:
    #         x_values = []
    #         x_values.append(y.get_x)
    #         t_values = []
    #         t_values.append(y.get_t)
    #     M1_X.append(x_values)
    #     M_T.append(t_values)
    # M0_X_arr = numpy.array(M0_X)
    # M0_T_arr = numpy.array(M0_T)

    plt.show
    #     for y in x:
    #         individual_x = []
    #         individual_x.append(y.get_x)
    #     M0_X.append(individual_x)
    # print(M0_points)

