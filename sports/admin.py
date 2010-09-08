from django.contrib import admin

from sports import models

class TeamAdmin(admin.ModelAdmin):
    """
    Display current members and coaches on the Team edit form.
    """
    #def render_change_form(self, request, context, add=False, change=False,
    #        form_url="", obj=None):
    #    if not change:
    #        return super(TeamAdmin, self).render_change_form(request, context,
    #                add, change, form_url, obj)
    #    context["current_players"] = obj.current_players()
    #    context["current_coaches"] = obj.current_coaches()

admin.site.register(models.Team, TeamAdmin)
admin.site.register([models.Person, models.League, models.LeagueTeam,
    models.TeamMember, models.LeagueUmpire])

