from django.http import HttpResponse
from django.shortcuts import render

def homePage(req):
    return render(req,'home/home.html')

def handling_404(req,exception):
    return render(req,'',{})
