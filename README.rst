==============================
Modeling Challenges In Django
==============================

Supporting code and slides for a talk originally given at DjangoCon-US,
September 2010 (in Portland, Oregon, USA).

Short Description
==================

How would you model players, umpires and coaches in baseball data when the same
person can switch roles over the course of their life? How about servers in
racks with power boards attached (and cords running across the room to remote
boards)? Here is one approach to create minimal and well-performing models for
such real-life situations. 

Abstract
=========

The slightly over-simplified but useful rule of thumb when creating database
schema is “normalize until it hurts, [then] denormalize until it works.” If
only people didn’t skip the first step so often. Using a data modeling layer,
such as Django's models, doesn't absolve the system architects from the need to
create good design. It also doesn't require them to do so, since you can get
away with a lot of sub-optimality with many data sets.

The real difficulty here, though, is that the trade-off between text-book ideal
modeling and easy to use is difficult to judge and takes practice to develop.

This talk will walk through some interesting cases of model design that I've
encountered recently. I'll explain how I approached the problem and what we
ended up with. These will include:

* Modeling people who might simultaneously play different roles in the system.
  For example, a person who was a baseball player and then became a coach —
  each role has different attributes attached to it.
* Modeling what appears to be a triangular dependency relationship with minimal
  redundancy in the data description and without needing really long query
  filters to access things.
* Handling date ranges (or other measured data) of different degrees of
  accuracy and precision.

This isn't a presentation on theoretical database design. Rather, concrete
examples of creating such designs and guiding the decisions by what might work
best in the final Django code. Hopefully, by listening to one person's approach
(mine!), people faced with similar challenges will have another possible attack
method in their toolbox.

Setup
======

Everything is configured to create an SQLite database and an automatic admin
user. Simply run::

    python manage.py syncdb --noinput

The admin user has username and password both set to *"admin"* (with the
quotes).

Tour of the code
=================

There are two applications included in this code package, providing models and
a brief amount of supporting code for the two cases covered in the
presentation.

The `dates/` application is a pair of simple models and is the easier of the
two cases. The `sports/` application is a tighter group of related models, that
has been reduced (over the course of the presentation) to something manageable.
The admin presentation for these models contains one enhancement: the team
display page includes extra information about the current members and coaches
(have a look in the templates directory to see how that is accomplished).

By default, both applications will be installed with sample data and are
viewable via Django's admin interface.

Good luck!

Malcolm Tredinnick
(Sydney, Australia)

