# encoding: utf-8
"""
author: yudd
time  : 2021.9.30
use   : to read excel file and find thermo key word
"""

import os
from analysis.thermo import find_thermo

def
if __name__ == '__main__':
    # file
    big_data = 'uniprot-had+family+phosphatase.xlsx'
    test_data = 'test-data.xlsx'

    # curr dir
    curr_dir = os.getcwd()            # /analysis-bacterium-temperature/analysis
    root_dir = os.path.abspath('..')  # /analysis-bacterium-temperature
    data_dir = os.path.join(root_dir, "data")
    xlsx_file = os.path.join(data_dir, big_data)

    # git absolute file path and file name suffix
    file_absolute_dir, file_name_suffix = os.path.splitext(xlsx_file)
    print(f'dir: {file_absolute_dir}, file: {file_name_suffix}')

    # set new file name
    is_thermo_xlsx = file_absolute_dir + '+is-thermo' + file_name_suffix
    no_thermo_xlsx = file_absolute_dir + '+no-thermo' + file_name_suffix
    print(f'new file: {is_thermo_xlsx}, {no_thermo_xlsx}')

    find_thermo(xlsx_file, is_thermo_xlsx, no_thermo_xlsx)




