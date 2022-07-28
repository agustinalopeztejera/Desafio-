from xmlrpc.client import DateTime
from django.shortcuts import render
from myfamily.models import Family_members

def create_family_member(request):
    new_member = Family_members.objects.create(name = 'John Smith', 
    age = 40, 
    hobbies = 'Playing football', 
    last_active_whapp = DateTime.now())

