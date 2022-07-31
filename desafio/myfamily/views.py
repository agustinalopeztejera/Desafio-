from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
from myfamily.models import Family_members


def my_dad(request):
   
    f = Family_members(name = 'John Smith',  age = 50,  hobbies = 'jugar al futbol', birthday = '1972-02-19')
    f.save()
    
    context = {'edad':'50', 'hobbies':'jugar al futbol', 'birthday':'1972-02-19'}
    return render(request, 'template_my_dad.html', context=context)


def my_mom(request):
   
    f = Family_members(name = 'Anna Smith',  age = 40,  hobbies = 'pintar', birthday = '1982-01-13')
    f.save()
    
    
    context = {'edad':'40', 'hobbies':'pintar', 'birthday': '1982-01-13'}
    return render(request, 'template_my_mom.html', context=context)

def my_bro(request):
   
    f = Family_members(name = 'Luke Smith',  age = 21,  hobbies = 'tocar la guitarra', birthday = '2000-10-23')
    f.save()
    
    
    context = {'edad':'21', 'hobbies':'tocar la guitarra', 'birthday': '2000-10-23'}
    return render(request, 'template_my_bro.html', context=context)


