from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Salut le monde, jsp pourquoi je fais du python mais bon voilà")
