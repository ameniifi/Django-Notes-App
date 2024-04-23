from django.shortcuts import render ,HttpResponse
from .models import Note
# Create your views here.

def name(request,nickname):
    print(nickname)
    return HttpResponse(f'Hello {nickname}')

def showAll(request):
    notes = Note.objects.all()
    return render(request,'index.html',context = {'notes':notes})

def showOne(request,id):
    note = Note.objects.get(id=id)
    if request.method == 'POST' :
        note.delete()
    return render(request,'note.html',context={'note':note})

def deleteOne(request,id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.delete()
        return HttpResponse('Deleted')