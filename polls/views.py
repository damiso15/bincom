from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import AgentName, AnnouncedLGAResults, AnnouncedPUResults, AnnouncedStateResults, AnnouncedWardResults, \
    LGA, Party, PollingUnit, States, Ward

# Create your views here.


class PollingUnitListView(generic.ListView):
    model = PollingUnit
    context_object_name = 'poll_list'
    queryset = PollingUnit.objects.only('unique_id', 'polling_unit_name')
    template_name = 'index.html'


def polling_unit_detail_view(request, pk):
    poll = get_object_or_404(PollingUnit, pk=pk)
    abbrev = AnnouncedPUResults.objects.all().filter(polling_unit_unique_id=pk)
    print(abbrev)
    context = {
        'poll': poll,
        'abbreviations': abbrev,
    }
    print(poll, 'this is working')
    return render(request, 'pollingunit_detail.html', context)

