# encoding: utf-8
"""
author: yudd
time  : 2021.10.1
use   : main

"""
import os
from analysis import thermo


class Args:
    def __init__(self):
        # file
        xlsx = 'uniprot-had+family+phosphatase.xlsx'
        test_data = 'test-data.xlsx'
        # file = "uniprot-had+family+phosphatase+is-thermo.xlsx"

        # curr dir
        curr_dir = os.getcwd()  # /analysis-bacterium-temperature/analysis
        # print(curr_dir)
        root_dir = os.path.abspath('..')  # /analysis-bacterium-temperature
        # print(root_dir)  # C:\\pytorch\\tdata

        data_dir = os.path.join(root_dir, "data")
        # print(data_dir)

        self.xlsx_file = os.path.join(data_dir, xlsx)
        self.source_file = self.xlsx_file
        # print(self.xlsx_file)

        # git absolute file path and file name suffix
        file_absolute_dir, file_name_suffix = os.path.splitext(self.xlsx_file)
        # print(f'dir: {file_absolute_dir}, file: {file_name_suffix}')

        # set new file name
        self.is_thermo_xlsx = file_absolute_dir + '+is-thermo' + file_name_suffix
        self.no_thermo_xlsx = file_absolute_dir + '+no-thermo' + file_name_suffix
        # print(f'new file: {self.is_thermo_xlsx}, {self.no_thermo_xlsx}')

        # set database file
        self.database = os.path.join(data_dir, "bacterium.xlsx")
        self.database2 = os.path.join(data_dir, "res-temp.xlsx")

        # create database temperature xlsx
        self.temperature = os.path.join(data_dir, "temperature.csv")
        self.temperature2 = os.path.join(data_dir, "temperature5.csv")

        # sqlite
        self.sqlite = os.path.join(data_dir, "database.db")

        # query res file
        self.query_result_no_thermo = file_absolute_dir + '+query-no-thermo' + file_name_suffix
        self.query_result_temperature = file_absolute_dir + '+thermo' + file_name_suffix
        self.query_result_only_thermo = os.path.join(data_dir, "result.xlsx")


class Log:
    def __init__(self):
        self._is_print = True

    def is_print(self, is_bool_print):
        self._is_print = is_bool_print

    def append(self, strs):
        if self._is_print:
            print(strs)


if __name__ == '__main__':
    args = Args()
    print(args.query_result_no_thermo)





