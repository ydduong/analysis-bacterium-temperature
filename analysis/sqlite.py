# encode=utf-8
"""

"""
import os
import sys
import csv
import sqlite3
from analysis import main


class Sqlite(object):
    def __init__(self, db):

        # check file
        _db_is_exist = True
        if not os.path.exists(db):
            _db_is_exist = False

        self._db = db
        self.connect = sqlite3.connect(self._db)
        self.cursor = self.connect.cursor()

        if not _db_is_exist:
            self.create_table()

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

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connect.close()


if __name__ == '__main__':
    args = main.Args()
    print(f'db: {args.sqlite}')

    delete = False
    if delete:
        os.remove(args.sqlite)

    database = Sqlite(args.sqlite)

    # insert data
    # database.executemany(args.temperature)

    # test select
    res = database.select('Candidatus Wildermuthbacteria')
    # []
    # [(12, 'Candidatus Wildermuthbacteria', 'https://webshop.dsmz.de/index.php?lang=1&cl=search&searchparam=Candidatus+Wildermuthbacteria', 'None', 'None')]
    print(res)
    print(res[0][4])

    print('ok')
    pass
