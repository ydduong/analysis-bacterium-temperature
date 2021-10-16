# encoding: utf-8
"""
author: yudd
time  : 2021.10.1
use   : main

"""
import os
from temperature import thermo


class Args:
    def __init__(self):
        # source excel file
        source_xlsx = 'source-data.xlsx'

        # root dir: above analysis-bacterium-temperature dir
        root_dir = os.path.abspath('../..')

        # dir of xlsx
        data_dir = os.path.join(root_dir, "data", "temperature")

        # absolute path for source xlsx file
        self.source_xlsx_file = os.path.join(data_dir, source_xlsx)

        # get absolute file path and file name suffix
        file_absolute_dir, file_name_suffix = os.path.splitext(self.source_xlsx_file)

        # the source xlsx file is divided into the following two files according to the thermo keyword
        self.is_thermo_source_xlsx_file = file_absolute_dir + '+is-thermo' + file_name_suffix
        self.no_thermo_source_xlsx_file = file_absolute_dir + '+no-thermo' + file_name_suffix

        # clean and remove duplicates data the organism column of no thermo keyword xlsx file
        self.no_thermo_bacterium_name_xlsx_file = os.path.join(data_dir, "no-thermo-bacterium-name.xlsx")

        # spider bacterium temperature, save search url、detail url and temperature
        self.spider_bacterium_temperature_csv_file = os.path.join(data_dir, "spider-bacterium-temperature.csv")

        # bacterium temperature database => bacterium(id bacterium_name search_url detail_url temperature)
        self.sqlite_bacterium_temperature_db = os.path.join(data_dir, "bacterium-temperature-database.db")

        # query no thermo xlsx file from database
        self.query_source_no_thermo_xlsx_result_file = file_absolute_dir + '+query-source-no-thermo-result' + file_name_suffix

        # source xlsx file => finally result file (thermo and than 50)
        self.all_result_xlsx_file = os.path.join(data_dir, "result.xlsx")


if __name__ == '__main__':
    args = Args()





