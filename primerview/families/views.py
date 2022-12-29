from django.shortcuts import render

from django.http import HttpResponse
from families.models import Families
# Create your views here.



def create_familiar(request):
    new_familiar = Families.objects.create(name='Juan Perez', age = 45, sex=True)
    print(new_familiar)
    return HttpResponse('Se creo el nuevo familiar')

def list_familiares(request):
    all_familiares = Families.objects.all()
    print(all_familiares)
    context = {
        'familiares':all_familiares,
    }
    return render(request, 'list_familiares.html', context=context)