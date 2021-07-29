from django.shortcuts import render
from django.http import HttpResponse
from .models import FAQ
# Create your views here.


def index(request):
    return HttpResponse("<h1>Medical Aid app 2 Homepage</h1>")



def faq(request):
    
    faqs = FAQ.objects.all()
    context = {
        "faqs": faqs 
    }
    return render(request,'aidApp/faq.html',context)