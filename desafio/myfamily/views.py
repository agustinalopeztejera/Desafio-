from multiprocessing import context
from xmlrpc.client import NOT_WELLFORMED_ERROR
from django.shortcuts import render
from datetime import datetime
from myfamily.models import Family_members


def my_dad(request):
   
    f = Family_members(name = 'John Smith',  age = 50,  hobbies = 'playing football')
    f.save()
    
    context = {"edad":"50", "hobbies":'playing football'}
    return render(request, 'template_my_dad.html', context=context)


def my_mom(request):
   
    f = Family_members(name = 'Anna Smith',  age = 40,  hobbies = 'knitting')
    f.save()
    
    
    context = {"edad":"50", "hobbies":'knitting', }
    return render(request, 'template_my_mom.html', context=context)

def my_bro(request):
   
    f = Family_members(name = 'Luke Smith',  age = 22,  hobbies = 'playing the guitar')
    f.save()
    
    
    context = {"edad":"50", "hobbies":'playing the guitar', }
    return render(request, 'template_my_bro.html', context=context)


