
from django.urls import path

from document.views import WhoWeAreListView, MissionVisionListView, BoardOfDirectorViewList, MessageFromCEOListView, \
    ManagementListView, CorporateFacilitiesServiceViewList

urlpatterns = [
    path('who-we-are/', WhoWeAreListView, name="who.we.are"),
    path('mission-vision/', MissionVisionListView, name="Mission.Vision"),
    path('board-of-director/',BoardOfDirectorViewList, name="board.of.director"),
    path('message-from-CEO/',MessageFromCEOListView, name="message.from.ceo"),
    path('management/',ManagementListView, name="management"),
    path('corporate-facilities-service/',CorporateFacilitiesServiceViewList, name="corporate.facilities.service"),
]
