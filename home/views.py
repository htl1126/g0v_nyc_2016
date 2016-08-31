from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('g0v Hackathon NYC 2016')
