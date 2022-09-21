from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import MshopModel


def index(request):
    return HttpResponse("App Home")

def mshop(request):
    ms=MshopModel()
    ms.mobilename="realme"
    ms.mobileram="4"
    ms.mobilerom="32"
    ms.mobilecolour="orange"
    ms.mobilebattery="5000mah"
    ms.price="16657"



    ms.save()
    return render(request,"mshop.html",)
