from django.shortcuts import render
from iphoneapp.models import iphone14
# Create your views here.
def iphone14view(request):
    iphone14list=iphone14.objects.all()
    dict1={'iphone14list':iphone14list}
    return render(request,'iphoneapp/iphone.html',context=dict1);
