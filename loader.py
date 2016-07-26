import os
from io import StringIO
from psycopg2 import connect
from psycopg2.extras import DictCursor


env = os.environ.get('RUN_ENV', None)


def db_connect():
    if env == 'test':
        dbname = os.environ.get("DB_NAME", "postgres")
        DSN = "dbname=%s user=postgres connect_timeout=5 keepalives_interval=5" % (dbname,)
    else:
        DSN = 'host=127.0.0.1 dbname=loader user=loader password=loader connect_timeout=5 keepalives_interval=5'

    db=connect(DSN)
    cursor=db.cursor(cursor_factory = DictCursor)
    if not cursor:
        raise Exception
    return cursor


def load_csv_file(file = None):
    if file is not None:
        cursor=db_connect()
        cursor.copy_expert(sql = "copy calls from STDIN DELIMITER ';' CSV", file = file)
        cursor.execute("COMMIT")


def create_table():
    SQL = 'create table if not exists calls (records_set text, start_epoch bigint NOT NULL, finish_epoch bigint NOT NULL, ext_epoch bigint,    from_extension int, from_number text, to_extension int, to_number text, result_code int, ext_number text, disconnect_reason text)'
    cursor = db_connect()
    cursor.execute(SQL)
    cursor.execute("COMMIT")



def main():
    load_from_csv()


if __name__ == '__main__':
    main()
