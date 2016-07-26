import unittest
from io import StringIO

from loader import load_csv_file, db_connect, create_table


class TestLoader(unittest.TestCase):
    def test_db_loader(self):
        CSV = u"""[];1411253533;1411253594;1411253578;;9442;;8425;0;47907;abonent
[];1411293133;1411293161;1411293148;;8062;;8425;0;47907;abonent
[];1411293186;1411295641;1411293200;;8062;;8425;0;47907;abonent
[];1411294125;1411294151;1411294142;;5060;;9999;0;47907;abonent
[];1411302615;1411302666;1411302660;;0207;;8425;0;47907;abonent
[];1411302687;1411303140;1411302708;;0207;;8425;0;47907;abonent
[];1411304057;1411304113;1411304074;;3647;;8425;0;47907;abonent
[];1411378185;1411378226;1411378197;;0505;;8425;0;47907;abonent
[];1411378319;1411379079;1411378333;;5555;;8425;0;47907;abonent
[];1411383991;1411384154;1411384003;;8779;;8425;0;47907;abonent
[];1411384708;1411384750;1411384718;;9999;;8425;0;47907;abonent
[];1411384731;1411384749;1411384742;;8425;;5321;0;47907;abonent
[];1411386079;1411386342;1411386090;;8016;;8425;0;47907;abonent
[];1411397448;1411397733;1411397465;;8062;;8425;0;47907;abonent
[];1411450751;1411450816;1411450796;;1734;;8425;0;47907;abonent
[];1411454718;1411454753;1411454735;;2711;;8425;0;47907;abonent
[];1411457704;1411457833;1411457714;;0125;;8425;0;47907;abonent"""

        cursor = db_connect()
        create_table()
        cursor.execute("SELECT COUNT(*) from calls")
        lines_count_before = cursor.fetchone()[0]
        f = StringIO(CSV)
        load_csv_file(file=f)
        cursor.execute("SELECT COUNT(*) from calls")
        lines_count_after = cursor.fetchone()[0]
        self.assertEqual(lines_count_before + 17, lines_count_after)

if __name__ == '__main__':
    unittest.main()
