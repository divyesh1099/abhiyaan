from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    sportlist=Sportlist.objects.all()[0]
    sports=Sport.objects.all()
    isports=Sport.objects.filter(door="Indoor")
    osports=Sport.objects.filter(door="Outdoor")
    print(isports)
    print(osports)
    return render(request, "sports/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports": sports,
        "isports": isports,
        "osports": osports,
        "sportlist":sportlist
        
    })

def isport(request):
    sports=Sport.objects.all()
    isports=Sport.objects.filter(door="Indoor")
    print("Indoor page is rendering")
    print(isports)
    return render(request, "sports/door.html", {
        "tsports":isports,
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":sports,
        "door":"Indoor"

    })

def osport(request):
    sports=Sport.objects.all()
    osports=Sport.objects.filter(door="Outdoor")
    print("Out door")
    print(osports)
    return render(request, "sports/door.html", {
        "tsports":osports,
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":sports,
        "door":"Outdoor"
    })

def sport(request, sport):
    sportlist=Sportlist.objects.all()[0]
    sports=Sport.objects.all()
    tsport=Sport.objects.get(name=sport)
    print("---------------------------")
    return render(request, "sports/sport.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports": sports,
        "sport":tsport,
        "sportlist":sportlist
    })