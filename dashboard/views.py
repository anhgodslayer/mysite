from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'dashboard/dashboard.html')
def data(request):
    return render(request,'dashboard/data.html')