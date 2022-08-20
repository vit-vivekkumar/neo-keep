from django.shortcuts import render,redirect

from django.views import generic
import requests
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


from api.models import Task
from api.views import *
from api.serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
def dashboard(request):
    response=requests.get('https://iamneo-keep.herokuapp.com/api/task-list/').json()
    if request.method=="POST":
        title = request.POST.get('title')
        note = request.POST.get('note')
        data={'title':title,'note':note}
        headers={'Content-Type':'application/json'}
        read =requests.post('https://iamneo-keep.herokuapp.com/api/task-create/',json=data,headers=headers)
        return redirect('dashboard')
    else:
        return render(request,'dashboard/index.html',{'response':response})

def delete_post(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('dashboard'))




def update_post(request, pk):
    notes= Task.objects.filter(id=pk).first()
    response=requests.get('https://iamneo-keep.herokuapp.com/api/task-list/').json()
    if request.method == 'POST':
        notes.title=request.POST['title']
        notes.note=request.POST['note']
        notes.save()
        return redirect('dashboard')
    else:
        return render(request,'dashboard/index.html',{'notes':notes, 'response':response})

    
    

def searchNote(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        notes =Task.objects.filter(title__contains=searched)
        return render(request,'dashboard/search.html',{'searched':searched,
            'notes':notes})
    else:
        return render(request,'dashboard/search.html',{})

