# Create your views here.
from django.http import HttpResponse

from annoying.decorators import render_to

from django.views.decorators.http import require_POST

from .forms import ComingSoonInterestForm


@render_to('comingsoon.html')
def index(request):
    return {}


@require_POST
def comingsoon_email_submit(request):
    form = ComingSoonInterestForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse()
    else:
        return HttpResponse(status=400)
