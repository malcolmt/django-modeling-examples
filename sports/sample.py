"""
Creates some sample data to illustrate the sports models. This is also
available as a fixture (generated via this file).
"""

from datetime import date

from sports import models


PEOPLE = (
    "Fred Flintstone",
    "Barney Rubble",
    "Bam-Bam",
    "Pebbles",
    "Dino",
)

TEAMS = (
    "Bedrock Bumblebees",
    "Whackity-sacks",
)

LEAGUES = (
    "Premier",
    "Old-timers",
)

def load_samples():
    people = {}
    teams = {}
    leagues = {}
    for name in PEOPLE:
        obj = models.Person.objects.create(name=name)
        people[name] = obj
    for name in TEAMS:
        obj = models.Team.objects.create(name=name)
        teams[name] = obj
    for name in LEAGUES:
        obj = models.League.objects.create(name=name)
        leagues[name] = obj

    start = date(2000, 4, 12)
    end = date(2002, 6, 30)

    # Leagues
    models.LeagueUmpire(joined=start, departed=end,
            league=leagues["Old-timers"], umpire=people["Dino"]).save()
    models.LeagueTeam(joined=start, departed=end, league=leagues["Old-timers"],
            team=teams["Whackity-sacks"]).save()
    start = date(2002, 7, 1)

    # Umpires
    models.LeagueUmpire(joined=start,
            league=leagues["Premier"], umpire=people["Dino"]).save()

    # Teams in Leagues
    for team in ("Whackity-sacks", "Bedrock Bumblebees"):
        models.LeagueTeam(joined=start, league=leagues["Premier"],
                team=teams[team]).save()

    # Players in teams
    team = teams["Whackity-sacks"]
    for player in ("Fred Flintstone", "Barney Rubble"):
        models.TeamMember(joined=start, team=team, person=people[player],
                role=models.PLAYER).save()

    # Team coach
    models.TeamMember(joined=start, team=team, person=people["Pebbles"],
            role=models.COACH).save()

if __name__ == "__main__":
    load_samples()

