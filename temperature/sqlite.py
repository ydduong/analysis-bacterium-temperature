# encode=utf-8
"""
use : Establish a database according to the crawled information
"""
import os
import sys
import csv
import sqlite3
from temperature import args


class Sqlite(object):
    def __init__(self, db, is_create_db=False, insert_data_file=None):
        # if not create database and db file is not exist -> exit
        if (not is_create_db) and (not os.path.exists(db)):
            print(f'database file is not exist.')
            sys.exit(1)
        else:
            print(f'sqlite using -> {db}')

        # if want create database and db file is exist -> delete this file first
        if is_create_db and os.path.exists(db):
            os.remove(db)

        self._db = db
        self.connect = sqlite3.connect(self._db)
        self.cursor = self.connect.cursor()

        if is_create_db:
            self.create_table()
            if os.path.exists(insert_data_file):
                self.executemany(insert_data_file)
            else:
                print(f'insert data file is None')

    def create_table(self):
        self.cursor.execute('''
            create table bacterium(
                id integer primary key autoincrement,
                bacterium_name text,
                search_url text,
                target_ulr text,
                temperature text
            )
        ''')

    def executemany(self, file):
        # example:
        # sql = 'insert into bacterium (bacterium_name, search_url, target_ulr, temperature) values (?, ?, ?, ?);'
        # data_list = [(1, '/etc/sysconfig', 'openshift_option', 'f'), (1, '/usr/share/doc', 'adb-utils-1.6', 'd')]

        # check file
        if not os.path.exists(file):
            print(f'file not exist: {file}')
            sys.exit(1)
        else:
            print(f'sqlite using -> {file}')

        # set data
        _data = []
        with open(file, "r") as f:
            _rows = csv.reader(f)
            for _row in _rows:
                _data.append(tuple(_row))

        _sql = 'insert into bacterium (bacterium_name, search_url, target_ulr, temperature) values (?, ?, ?, ?);'

        try:
            self.cursor.executemany(_sql, _data)
            self.connect.commit()
        except Exception as e:
            self.connect.rollback()
            raise Exception(f"executemany failed: {e}")

    def select(self, word):
        _sql = f'select * from bacterium where bacterium_name="{word}"'

        try:
            _res = self.cursor.execute(_sql).fetchall()
            # print(type(_res))
            return _res
        except Exception as e:
            raise Exception(f'select failed: {_sql}\nerror: {e}')

    def get_table_rows_num(self):
        _sql = f'select count(*) from bacterium;'
        try:
            _res = self.cursor.execute(_sql).fetchall()
            # print(type(_res))
            print(f'table row number: {_res[0][0]}\n')
        except Exception as e:
            raise Exception(f'select failed: {_sql}\nerror: {e}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    args = args.Args()

    # param: bd file; is create a new db: insert data file
    database = Sqlite(args.sqlite_bacterium_temperature_db, True, args.spider_bacterium_temperature_csv_file)

    # # test select
    # res = database.select('Marinovum')
    # # []
    # # [(12, 'Candidatus Wildermuthbacteria', 'https://webshop.dsmz.de/index.php?lang=1&cl=search&searchparam=Candidatus+Wildermuthbacteria', 'None', 'None')]
    # print(res)
    # print(res[0][4])

    database.get_table_rows_num()

