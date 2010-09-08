# coding: utf-8
"""
The Challenge: Create a useful way of modeling dates — both a single point in
time and a start and end point — that have varying levels of precision
attached. The date might be trying to indicate anything from a specific day, or
a whole year, or an entire century.

We aren't going to deal with the problem of modeling error bars on dates (such
as 1753 ± 18 years), although similar techniques could be used for that case.
One date model is not appropriate for every single situation.
"""

import datetime

from django.db import models


PRECISION_CHOICES = (
    (0, "precise"),
    (1, "month"),
    (2, "year"),
    (3, "decade"),
    (4, "century"),
)

class Date(models.Model):
    """
    Dates with precision measurements. This class is a little naïve when it
    comes to really ancient dates: it doesn't take calendar changes into
    consideration. Every year has 365 days, for example (if you think that's
    a given, look at September, 1752 when you have a spare moment).
    """
    date = models.DateField()
    precision = models.IntegerField(default=0, choices=PRECISION_CHOICES)

    def __unicode__(self):
        """
        An intentionally naïve display of the relevant data. Most displays of
        dates will want to format things differently to this, but we'll leave
        the specifics to utility functions and focus on genericity in this
        method.
        """
        # XXX: Work around fact that strftime() cannot usually handle years
        # prior to 1900.
        tmp_date = self.date.replace(year=1900)
        date_str = u"%s, %s" % (tmp_date.strftime("%d %b"), self.date.year)
        if self.precision == 0:
            return date_str
        return u"%s containing %s" % (self.get_precision_display(), date_str)

    def canonical_version(self):
        """
        Returns a canoical version of the date. Useful for sorting and
        comparisons. This is earliest date in the interval.

        For example, 1/1/1903 and 6/6/1901 with decade precisions both have a
        canonical version of 1/1/1901 (with decade precision).

        Centuries and decades are both treated as starting on the year ending
        with "1" (e.g. 1901, rather than 1900).
        """
        precision = self.precision
        if precision == 0:
            return self.date
        if precision == 1:
            return datetime.date(1, self.date.month, self.date.year)
        if precision == 2:
            return datetime.date(1, 1, self.date.year)
        if precision == 3:
            new_year = 1 + 10 * ((self.date.year - 1) / 10)
            return datetime.date(1, 1, new_year)
        if precision == 4:
            new_year = 1 + 100 * ((self.date.year - 1) / 100)
            return datetime.date(1, 1, new_year)
        raise AssertionError("Bad data: should never have gotten here!")

class DateRange(models.Model):
    start = models.ForeignKey(Date, related_name="start_dates")
    end = models.ForeignKey(Date, null=True, related_name="end_dates")

    def __unicode__(self):
        if self.end:
            return u"%s to %s" % (self.start, self.end)
        return u"range starting %s" % self.start

