from django.shortcuts import render
from core.models import Category , Events , Service
# Create your views here.
def index(request):
    categories = Category.objects.all( )
    events = Events.objects.all()
    service = Service.objects.all()

    return render(request , 'core/index.html', {
        
        "events" :events,
        "categories":categories,
        "service":service,
        
        })



