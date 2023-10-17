#from django.views import generic
from django.http import HttpResponse

def index(request):
    return HttpResponse("Oué")
