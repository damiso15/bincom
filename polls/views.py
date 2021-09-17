from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import AgentName, AnnouncedLGAResults, AnnouncedPUResults, AnnouncedStateResults, AnnouncedWardResults, \
    LGA, Party, PollingUnit, States, Ward

# Create your views here.


def index_view(request):
    return render(request, 'index.html')


class PollingUnitListView(generic.ListView):
    model = PollingUnit
    context_object_name = 'poll_list'
    queryset = PollingUnit.objects.only('unique_id', 'polling_unit_name')
    template_name = 'pollingunit_list.html'


def polling_unit_detail_view(request, pk):
    poll = get_object_or_404(PollingUnit, pk=pk)
    abbrev = AnnouncedPUResults.objects.all().filter(polling_unit_unique_id=pk)
    if abbrev.count() == 0:
        raise Http404("Result for this Polling Unit is not yet out")
    context = {
        'poll': poll,
        'abbrev': abbrev,
    }
    return render(request, 'pollingunit_result.html', context)


class LGAListView(generic.ListView):
    model = LGA
    context_object_name = 'lga_list'
    queryset = LGA.objects.only('lga_name')
    template_name = 'lga_list.html'


def lga_detail_view(request, pk):
    lga = get_object_or_404(LGA, lga_id=pk)
    poll = PollingUnit.objects.all().filter(pk=pk)
    result = AnnouncedPUResults.objects.all().filter(polling_unit_unique_id=pk)
    if result.count() == 0:
        raise Http404("Result for this Local Government is not out.")
    result_list = []
    for item in result:
        cal = item.party_score
        result_list.append(cal)
    result_sum = sum(result_list)
    print(lga)
    print(poll)
    context = {
        'lga': lga,
        'poll': poll,
        'result': result,
        'result_sum': result_sum,
    }
    print(result, 'this is working')
    return render(request, 'lgapolling_result.html', context)
