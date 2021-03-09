from django.shortcuts import render # ส่วนของการให้ render ของหน้าเว็บนั้นๆ
#from django.http import HttpResponse // ตัดออก 9 กพ

# Create your views here.
def index(request):
    return render(request,'index.html')
    #Hello Hiblood Donation

def product(request):
    return render(request,'product.html')
