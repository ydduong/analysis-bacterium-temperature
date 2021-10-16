# encode=utf-8
import urllib3
from temperature.args import Args
from temperature.thermo import find_thermo
from temperature.bacterium import preprocessing
from temperature.spider import Spider
from temperature.sqlite import Sqlite
from temperature.query import query

if __name__ == '__main__':
    args = Args()

    # param: source excel file; save thermo data xlsx; save no thermo data xlsx
    find_thermo(args.source_xlsx_file, args.is_thermo_source_xlsx_file, args.no_thermo_source_xlsx_file)

    # param: source xlsx file without thermo keyword; only save bacterium name
    preprocessing(args.no_thermo_source_xlsx_file, args.no_thermo_bacterium_name_xlsx_file)

    urllib3.disable_warnings()
    # param: bacterium names; to save bacterium information csv file
    spider = Spider(args.no_thermo_bacterium_name_xlsx_file, args.spider_bacterium_temperature_csv_file)
    spider.run()

    # param: bd file; is create a new db: insert data file
    database = Sqlite(args.sqlite_bacterium_temperature_db, True, args.spider_bacterium_temperature_csv_file)
    database.get_table_rows_num()

    query(args.sqlite_bacterium_temperature_db, args.source_xlsx_file, args.query_source_no_thermo_xlsx_result_file,
          args.all_result_xlsx_file)


