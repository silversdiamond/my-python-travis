import unittest
import datetime

from dateutil.relativedelta import relativedelta

from time_walker import walk


class TestLoader(unittest.TestCase):
    def test_walker(self):
        start_ts = datetime.datetime.strptime("01/09/14", "%d/%m/%y")
        end_ts = datetime.datetime.strptime("16/09/16", "%d/%m/%y")
        interval = relativedelta(days=10)
        res = list(walk(start_ts, end_ts, interval))
        result = (datetime.datetime(2014, 9, 11, 0, 0),
                  datetime.datetime(2014, 9, 21, 0, 0))
        self.assertEqual(res[1], result)

    def test_10_days_intervals_count(self):
        start_ts = datetime.datetime.strptime("01/09/14", "%d/%m/%y")
        end_ts = datetime.datetime.strptime("16/09/14", "%d/%m/%y")
        self.assertEqual(sum(1 for item in walk(start_ts, end_ts,
                             relativedelta(days=10))), 2)

    def test_negative_result_end_date(self):
        end_ts = datetime.datetime.strptime("16/09/14", "%d/%m/%y")
        self.assertEqual(sum(1 for item in walk(end_ts, end_ts,
                             relativedelta(days=10))), 0)

    def test_end_date_equal_start(self):
        end_ts = datetime.datetime.now()
        self.assertEqual(list(walk(end_ts, end_ts, relativedelta(days=1))), [])


if __name__ == '__main__':
    unittest.main()
