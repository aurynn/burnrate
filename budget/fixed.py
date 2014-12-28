import arrow
from .util import Span
import decimal

frequencies = {
        "week": None,
        "month": "DD",
        "year": "MMMM DD"
        }

class Fixed(object):
    """
    Implements a fixed-cost bill, that recurs once per period of time.
    This will generally implement as either a monthly or yearly figure.

    """

    def __init__(self, cycle, frequency, amount, base=None, name=None):
        self.__frequency = frequency
        self.amount = decimal.Decimal(amount)
        if frequency == "week":
            return
        self.__base = base or arrow.now()
        fmt = frequencies.get(frequency)

        self.start = arrow.get(cycle, fmt).replace(year=self.__base.year)
        if frequency == "month":
            self.start = self.start.replace(month=self.__base.month)
        
        

        self.shifted_start = None

        self.end = self.start.replace(**{
            "{frequency}s".format(frequency=frequency) :
            1
            })
        self.name = name

    def prorate(self, start):
        self.shifted_start = start

    def weeks(self):
        s = Span("Thursday") # TODO: Don't hardcode this

        start = self.shifted_start or self.start
        end = self.end
        return s.weeks(start, end)
    
    def per_week(self):
        """Returns the per-week cost of this fixed bill"""
        if self.__frequency == "week":
            return self.amount
        # Set precision to 2, for dealing with money amounts
        
        return self.amount / self.weeks()
