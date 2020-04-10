import unittest

from lambdata_axel.ds_tools import DSDataFrame

data = {'numbers': [0, 1, 2, 3, 4, 5, 6, 7],
        "alphabet": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}


class TestDSDataFrame(unittest.TestCase):
    def setUp(self):
        self.df = DSDataFrame(data)

    def test_check_nulls(self):
        columns = self.df.columns.tolist()
        self.assertEqual(len(columns), len(
            self.df.check_nulls().values), 'incorrect columns size')


if __name__ == "__main__":
    unittest.main()
