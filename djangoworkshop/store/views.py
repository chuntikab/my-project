from django.shortcuts import render
#from django.http import HttpResponse // ตัดออก 9 กพ

# Create your views here.
def index(request):
    return render(request,'index.html')
#Hello Hiblood Donation
