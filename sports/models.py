"""
In many sports, a person can play one (or more) of multiple roles: player,
coach or umpire/referee, for example.

For our purposes here, an umpire is associated with a league (of which there
can be more than one), whilst players and coaches are associated with teams,
which make up the leagues. A single person can have multiple roles over time,
sometimes more than one at a time (e.g. player-coach).
"""

from django.db import models


COACH = "C"
PLAYER = "P"

class Person(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "people"

    def __unicode__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def current_coaches(self):
        return Person.objects.filter(teammember__team=self,
                teammember__role=COACH).order_by("name")

    def current_players(self):
        return Person.objects.filter(teammember__team=self,
                teammember__role=PLAYER).order_by("name")


class League(models.Model):
    name = models.CharField(max_length=100)
    umpires = models.ManyToManyField(Person, through="LeagueUmpire")
    teams = models.ManyToManyField(Team, through="LeagueTeam")

    def __unicode__(self):
        return self.name


class Membership(models.Model):
    """
    A specification of belonging to something for a period of time. Concrete
    base classes with supply the "somethings".
    """
    joined = models.DateField()
    departed = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

    def _to_string(self, lhs, rhs):
        pairing = u"%s - %s" % (lhs, rhs)
        if self.departed:
            return u"%s (%s - %s)" % (pairing,
                    self.joined.strftime("%d %b %Y"),
                    self.departed.strftime("%d %b %Y"))
        return u"%s (%s - )" % (pairing, self.joined.strftime("%d %b %Y"))


class LeagueMembership(Membership):
    league = models.ForeignKey(League)

    class Meta:
        abstract = True

    def _to_string(self, lhs):
        return super(LeagueMembership, self)._to_string(lhs, self.league)


class LeagueTeam(LeagueMembership):
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self._to_string(self.team)


class LeagueUmpire(LeagueMembership):
    umpire = models.ForeignKey(Person)

    def __unicode__(self):
        return self._to_string(self.umpire)


class TeamMember(Membership):
    team = models.ForeignKey(Team, related_name="members")
    person = models.ForeignKey(Person)
    role = models.CharField(max_length=2,
            choices=((COACH, "coach"), (PLAYER, "player")))

    def __unicode__(self):
        return self._to_string(self.team, self.person)

