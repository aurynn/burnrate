import arrow

day_mapping = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
]

class Span(object):
    def __init__(self, start_of_week):
        if isinstance(start_of_week, str):
            self.sow = day_mapping.index( start_of_week )
        elif isinstance(start_of_week, int) and start_of_week < len(day_mapping):
            self.sow = start_of_week
        else:
            raise ValueError("Start day {d} out of range".format(start_of_week))

    def weeks(self, start, end):
        assert(isinstance(start, arrow.arrow.Arrow))
        assert(isinstance(end, arrow.arrow.Arrow))
        weeks = 0 
        if start.weekday() > self.sow:
            weeks -= 1
        
        if end.weekday() < self.sow:
            weeks -= 1

        vals = arrow.Arrow.range("weeks", start, end)
        weeks += len(vals)
        
        if end.isocalendar()[1] != vals[-1].isocalendar()[1]:
            weeks += 1
        
        return weeks




