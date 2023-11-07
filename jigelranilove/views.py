from django.shortcuts import render
from django.http import HttpResponse

def jigelrani(request):
    return HttpResponse("<h1 style = 'color:green'><marquee>Hi My Name Is Jigelrani</h1></marquee>")



def chittibabu(request):
    return HttpResponse("<h1 style = 'color:red'><marquee>Hi My Name Is Chittibabu</h1></marquee>")

# Create your views here.
