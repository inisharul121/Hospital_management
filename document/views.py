from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from document.models import WhoWeAre, MissionVision, BoardOfDirector, MessageFromCEO, Management,CorporateFacilitiesService


class WhoWeAre(ListView):
    model = WhoWeAre


WhoWeAreListView = WhoWeAre.as_view()

class MissionVision(ListView):
    model = MissionVision

MissionVisionListView=MissionVision.as_view()


class BoardOfDirector(ListView):
    model = BoardOfDirector

BoardOfDirectorViewList=BoardOfDirector.as_view()


class MessageFromCEO(ListView):
    model= MessageFromCEO

MessageFromCEOListView=MessageFromCEO.as_view()


class Management(ListView):
    model= Management

ManagementListView=Management.as_view()


class CorporateFacilitiesService(ListView):
    model= CorporateFacilitiesService

CorporateFacilitiesServiceViewList=CorporateFacilitiesService.as_view()

