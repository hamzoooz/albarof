from django.shortcuts import render
from core.models import Category , Events , Service , SubServers
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

# C:\hamza\files\django\albarof\templates\inc\parts\subservices.html
def subservice(request , id ):
    
    subservice = SubServers.objects.filter(id=id)
    # subservice
    return render(request , 'core/subservices.html', { "subservice":subservice, })

