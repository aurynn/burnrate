import unittest
import arrow
from burnrate.fixed import Fixed
import decimal

class TestFixedBudget(unittest.TestCase):
    
    def setUp(self):
        self.base = arrow.get("December 05, 2014", "MMMM DD, YYYY")

    def test_default_weekly(self):
        base = arrow.get("December 05, 2014", "MMMM DD, YYYY")
        f = Fixed("05", "month", 100, base)
        self.assertTrue(f.weeks() == 4)
        self.assertTrue(f.per_week() == 25)

    def test_prorate_weekly(self):

        base = arrow.get("December 05, 2014", "MMMM DD, YYYY")
        f = Fixed("05", "month", 100, base)
        f.prorate(base.replace(weeks=+1))
        self.assertTrue(f.weeks() == 3)
        decimal.getcontext().prec = 2
        self.assertTrue(f.per_week() == decimal.Decimal(100) / 3)

    def test_base_yearly(self):

        f = Fixed("December 05", "year", 520, self.base)
        self.assertTrue(f.weeks() == 52)
        self.assertTrue(f.per_week() == 10)
