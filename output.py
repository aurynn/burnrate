#from budget.fixed import Fixed
from budget.origin import origin
import arrow
import begin
import json
import decimal

@begin.start
def run(*files):
    with origin(arrow.get("December 05, 2014", "MMMM DD, YYYY")) as start:
        for fn in files:
            data = json.loads(open(fn).read())
            bills = []
            for key in data.keys():
                k = key.replace("ly", "")
                for name, deets in data[key].iteritems():
                    f = start.fixed(deets["date"], k, deets["amount"], name=name)
                    now = arrow.now()
                    # Should we prorate or not?
                    bills.append(f)
            a = [b.per_week() for b in bills] 
            print sum(a).quantize(decimal.Decimal("1.00"))
