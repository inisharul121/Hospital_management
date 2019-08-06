from django.contrib import admin

# Register your models here.
from document.models import WhoWeAre, MissionVision, BoardOfDirector, MessageFromCEO, Management, \
    CorporateFacilitiesService

admin.site.register(WhoWeAre)
admin.site.register(MissionVision)
admin.site.register(BoardOfDirector)
admin.site.register(MessageFromCEO)
admin.site.register(Management)
admin.site.register(CorporateFacilitiesService)