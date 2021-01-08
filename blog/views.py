from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def indx(requtes):
    return  render(requtes,'blog/indx.html')
