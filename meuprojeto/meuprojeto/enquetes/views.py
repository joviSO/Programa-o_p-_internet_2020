from django.shortcuts import render
from enquetes.models import Enquete 

def bemvindo(request):
    return render(request, 'index.html')

def enquete(request,enquete_id):
    enquete = Enquete()
    if enquete_id == 1:
        enquete = Enquete('A vida é que em rapadura é doce mas, não é mole não', '21:10 27/08/2020')
    if enquete_id == 2:
        enquete = Enquete('Água mole em pedra dura tanto bate até que fura', '04:03 28/08/2020')
    if enquete_id == 3:
        enquete = Enquete('Quanto mais dias vivemos, menos dias temos', '10:54 29/08/2020')
 
    
    return render(request, 'enquete.html', {"enquete":enquete})
# Create your views here.
