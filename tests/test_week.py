from burnrate.util import Span
import unittest
import arrow

class TestUtils(unittest.TestCase):

    def test_span(self):
        s = Span("Thursday")
        start = arrow.get("December 1, 2014", "MMMM D, YYYY")
        end = arrow.get("January 1 2015", "MMMM D YYYY")
        self.assertTrue(s.weeks(start, end) == 5)
