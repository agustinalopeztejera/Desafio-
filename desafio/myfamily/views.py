from multiprocessing import context
from django.shortcuts import render
from datetime import datetime
from myfamily.models import Family_members

def my_dad(request):
    today = datetime.now()
    my_dad = Family_members.objects.create(name = 'John Smith', 
    age = '50', 
    hobbies = 'playing football',
    last_active_whapp = today)
    context = {context}
    return render(request, 'template_my_dad.html', context=context)
