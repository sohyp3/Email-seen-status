from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect

import random, string

from .models import infoModel,pingModel
from .forms import infoForm

def main (request):
    
    infoData = infoModel.objects.all()
    pingData = pingModel.objects.all()

    context = {
        'info':infoData,
        'ping':pingData,
    }
    return render(request, "index.html",context) 

def create(request):
    token = ''
    currentForm = infoForm()
    recieveFrom = infoForm(request.POST)

    if request.method =='POST': 
        if recieveFrom.is_valid():
            token = recieveFrom.cleaned_data['tracker']
            notes = recieveFrom.cleaned_data['notes']

            if token == "" or  token == " " or token == None:
                token = create_token()

            infoModel(tracker=token,clicked=False,notes=notes).save()

    context ={
        "link":token,
        "form" : currentForm
    }
    
    return render(request,"create.html",context)


def redirector(request,token):
    info = infoModel.objects.get(tracker=token)
    info.clicked = True
    info.save()

    pingModel(ip=ipGet(request),incoming=info).save()
    return HttpResponseRedirect('/images/lulw.png')



def delete(request,id):
    infoModel.objects.get(id=id).delete()
    return redirect("main")


def ipGet(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def create_token():
    token_size = 5
    letters = string.ascii_letters
    return "".join (random.choice(letters)for i in range (token_size))
