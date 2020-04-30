import datetime

from django.http import HttpResponse, Http404
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html',
                  {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'future_datetime.html',
                  {'hour_offset': offset,
                   'next_time': dt})
