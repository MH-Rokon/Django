from django.shortcuts import render
from django.http import HttpResponse

# def about_us(request):
#     return render(request,'base.html')
def about(request):
    return render(request,'index.html')


