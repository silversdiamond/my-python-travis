import datetime
import time

from dateutil.relativedelta import relativedelta


START_DATE = '01/09/14'
END_DATE = '16/09/16'


def walk(start_date=None, end_date=None, interval=None):
    if start_date >= end_date:
        return
    date_pointer = start_date
    while date_pointer + interval < end_date:
        next_pointer = date_pointer + interval
        yield (date_pointer, next_pointer)
        date_pointer = next_pointer
    yield (date_pointer, end_date)



def main():
    start_ts = datetime.datetime.strptime(START_DATE, "%d/%m/%y")
    end_ts = datetime.datetime.strptime(END_DATE, "%d/%m/%y")
    interval = relativedelta(days=10)
    for item in walk(start_ts, end_ts, interval):
        print(item)


if __name__ == '__main__':
    main()
