burnrate
=======

burnrate is a simple library for computing a weekly expenditure from a list of bills over a monthly and yearly cycle.

The core drive behind writing burnrate was that I wanted to know how much money I needed to put aside every week in order to cover a bill before it next hit.

burnrate makes the following assumptions:

	* You organize your finances on a weekly basis
	* Every "pay week" starts on Thursday

usage
------

simple example commandline tool
------

*output.py* implements a simple commandline tool to generate a burn rate.
it is run via
```
$ python output.py data.json
```

data.json is a set of information regarding your outputs, in the form:
```
{
 "weekly": {
  "weekly_project": {
   "amount": 100,
   "day": "Monday" # unused
  },
  ... # etc
},
 "monthly": {
  "some_project": {
   "date": "01",
   "amount": 100
  },
  ... # etc
 },
 "yearly": {
  "yearly_project: {
   "date": "January 01",
   "amount": 100
  },
  ... # etc
 }
}
```

