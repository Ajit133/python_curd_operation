from django.shortcuts import render
from django.http import HttpResponse
from .form.catagories import catagories
def index(request):
    form = catagories()

    diction = {"title": form}
    return render(request,'index.htm',context=diction)

