import unittest
from datetime import datetime
from avail_management.algorithm.finder import *

class TestFinder(unittest.TestCase):

    dates = []
    dates.append(KeyDate(2, True))
    dates.append(KeyDate(5, False))
    dates.append(KeyDate(1, True))
    dates.append(KeyDate(4, False))
    dates.append(KeyDate(3, True))
    dates.append(KeyDate(6, False))

    def test_find_within_max_capacity(self):
        print(find(max_capacity=10, today=datetime.today(), key_dates=dates))

    def test_find_exceed_max_capacity(self):
        print(find(max_capacity=2, today=datetime.today(), key_dates=dates))


if __name__ == '__main__':
    unittest.main()
