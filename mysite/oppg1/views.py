from django.shortcuts import render
import time
#from .forms import Utregning
# Create your views here.

def index(request): # Oppretter funksjonen index
    return render(request, 'oppg1/index.html')
    
    
"""    inntekt = 11000/30/24/60/60
    formue = 160000
    while 1:
        formue = formue + inntekt
        svarTilbake = "Eiriks netto formue: " + str(formue) + "."
        return render(request, 'oppg1/index.html', {'svarTilbake': svarTilbake})
        time.sleep(1)
        
    
"""