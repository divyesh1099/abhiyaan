from django.shortcuts import render
from days.models import Event as DaysEvents
from departmentalfests.models import Event as DepartmentalfestsEvents
from maineventsdayone.models import Event as MaineventsdayoneEvents
from maineventsdaytwo.models import Event as MaineventsdaytwoEvents
from maineventsdaythree.models import Event as MaineventsdaythreeEvents
from sports.models import Sport as Sports
# Create your views here.
def index(request):
    de=DaysEvents.objects.all()
    dfe=DepartmentalfestsEvents.objects.all()
    moe=MaineventsdayoneEvents.objects.all()
    mot=MaineventsdaytwoEvents.objects.all()
    moth=MaineventsdaythreeEvents.objects.all()
    se=Sports.objects.all()
    return render(request, "home/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"],
        "de":de,
        "dfe":dfe,
        "moe":moe,
        "mot":mot,
        "moth":moth,
        "se":se
    })

def search(request):
    if request.method=="POST":
        nq=request.POST['q']
        print(nq)
        # Now we an process this querry as to search in our database and show results
    return render(request, "home/index.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })

def about(request):
    return render(request, "home/about.html", {
        "days": ["Clan", "Corporate", "Traditional"],
        "departmentalfests": ["CSE", "IT", "EXTC", "ME", "CE"],
        "sports":["Kabaddi", "Kho-Kho", "Cricket", "Batminton"]
    })
