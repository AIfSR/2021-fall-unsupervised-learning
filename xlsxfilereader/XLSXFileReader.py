from xlsxfilereader.Episodes import Episodes
from xlsxfilereader.Episode import Episode
import os
import openpyxl
import xlwt, xlrd, re
from xlutils.copy import copy
import pandas as pd

class XLSXFileReader:
    
    def get_episodes(self, path_to_xlsx_file:str):
        """Gets all of the points from the specified XLSX file."""
        script = os.path.dirname(__file__)
        script1 = os.path.dirname(script)
        path = os.path.join(script1, path_to_xlsx_file)
        os.getcwd()
        data = pd.ExcelFile(path)
        df = data.parse('Sheet1')
        ps = openpyxl.load_workbook(path)
        sheet = ps['Sheet1']
        WK_episodes = Episodes()
        SWS_episodes = Episodes()
        PS_episodes = Episodes()
        all_episodes = Episodes()
        for row in range(3, sheet.max_row + 1):
            WK_N = sheet['A' + str(row)].value
            WK_Occ = sheet['B' + str(row)].value
            WK_Duration = sheet['C' + str(row)].value
            if WK_N != None and WK_Occ != None and WK_Duration != None:
                WK_episode = Episode("WK",WK_N, WK_Occ, WK_Duration)
                WK_episodes.addEpisode(WK_episode)
                all_episodes.addEpisode(WK_episode)

            SWS_N = sheet['E' + str(row)].value
            SWS_Occ = sheet['F' + str(row)].value
            SWS_Duration = sheet['G' + str(row)].value
            if SWS_N != None and SWS_Occ != None and SWS_Duration != None:
                SWS_episode = Episode("SWS",SWS_N, SWS_Occ, SWS_Duration)
                SWS_episodes.addEpisode(SWS_episode)
                all_episodes.addEpisode(SWS_episode)
            PS_N = sheet['I' + str(row)].value
            PS_Occ = sheet['J' + str(row)].value
            PS_Duration = sheet['K' + str(row)].value
            if PS_N != None and PS_Occ != None and PS_Duration != None:
                PS_episode = Episode("PS",PS_N, PS_Occ, PS_Duration)
                PS_episodes.addEpisode(PS_episode)
                all_episodes.addEpisode(PS_episode)
        all_episodes.sort()
        return all_episodes


