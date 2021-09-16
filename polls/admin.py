from django.contrib import admin
from .models import AgentName, AnnouncedLGAResults, AnnouncedPUResults, AnnouncedStateResults, AnnouncedWardResults, \
    LGA, Party, PollingUnit, States, Ward

# Register your models here.
admin.site.register(AgentName)
admin.site.register(AnnouncedLGAResults)
admin.site.register(AnnouncedPUResults)
admin.site.register(AnnouncedStateResults)
admin.site.register(AnnouncedWardResults)
admin.site.register(LGA)
admin.site.register(Party)
admin.site.register(PollingUnit)
admin.site.register(States)
admin.site.register(Ward)
