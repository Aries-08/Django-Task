from django.shortcuts import render
from django.template import loader
from firstPage.models import ipl
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
import json


def main_page(request):
    return render(request, 'index.html')

def graph_view(request):
    template = loader.get_template("stacked_bar_chart.html")
    return HttpResponse(template.render(request=request))


def graph_view_api(request):
    # distinct teams --> teams
    # seasons [s1,s2,s3] --> seasons
    # dict of no of matches played teams [x,y,z] --> teamCount
    teams = [item["team1"] for item in  ipl.objects.values("team1").distinct().order_by("team1")]
    # missed_teams = [item["team2"] for item in  ipl.objects.values("team2").distinct() if item["team2"] not in teams ]
    seasons = [item["season"] for item in  ipl.objects.values("season").distinct().order_by("season")]
    teamCount : dict = {}

    for team in teams: 
        teamCount[team] = [0]*len(seasons)
    print(teamCount)

    data_list1 = ipl.objects.values("team1", "season").annotate(matches=Count("id"))
    data_list2 = ipl.objects.values("team2", "season").annotate(matches=Count("id"))
    print(data_list1)

    for data in data_list1:
        teamCount[data["team1"]][seasons.index(data["season"])] = data["matches"]

    for data in data_list2:
        teamCount[data["team2"]][seasons.index(data["season"])] += data["matches"]
    
    print(teamCount)

    return JsonResponse({
        "status": "sucess",
        "data":  {
            "teamCount": teamCount,
            "seasons": seasons,
            "teams" : teams
        }
    })
