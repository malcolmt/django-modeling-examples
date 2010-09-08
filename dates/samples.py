"""
Some sample date data to use for experimenting with the Date and DateRange
models.

This data is loaded as part of an initial fixture if you ran "syncdb", but the
code is included here in order to regenerate things from scratch.
"""

from datetime import date, datetime

from dates import models


# All dates are in DD/MM/YYYY format. North Americans will have to mentally
# convert.
DATES = (
    ("01/11/1937", 0),  # precise
    ("01/08/1891", 1),  # month
    ("11/11/1975", 2),  # year
    ("5/4/1940", 3),    # decade
    ("1/1/1000", 4),    # century
)

DATE_RANGES = (
    ("1/1/0101", 4, "1/1/0400", 4),
    ("2/2/1201", 4, "30/6/1752", 3),
    ("1/1/1905", 3, "8/9/2010", 0),
)

OPEN_RANGES = (
    ("2/2/1201", 4),
    ("1/1/1905", 3),
)

def load_samples():
    for date_str, prec in DATES:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        models.Date(date=date, precision=prec).save()

    for date1_str, prec1, date2_str, prec2 in DATE_RANGES:
        date1 = datetime.strptime(date1_str, "%d/%m/%Y").date()
        date2 = datetime.strptime(date2_str, "%d/%m/%Y").date()
        obj1 = models.Date.objects.create(date=date1, precision=prec1)
        obj2 = models.Date.objects.create(date=date2, precision=prec2)
        models.DateRange(start=obj1, end=obj2).save()

    for date_str, prec in OPEN_RANGES:
        date = datetime.strptime(date_str, "%d/%m/%Y").date()
        obj = models.Date.objects.create(date=date, precision=prec)
        models.DateRange(start=obj).save()

if __name__ == "__main__":
    load_samples()

