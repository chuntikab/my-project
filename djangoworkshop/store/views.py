from django.shortcuts import render, get_object_or_404 # ส่วนของการให้ render ของหน้าเว็บนั้นๆ
from store.models import Category,Product
#from django.http import HttpResponse // ตัดออก 9 กพ

# Create your views here.
def index(request,category_slug=None): # หน้าแรก
    products=None
    category_page=None
    if category_slug != None: # ถ้าค่า category slug != None
        category_page=get_object_or_404(Category,slug=category_slug) # ทำการค้นหาหมวดหมู่ category 
        products=Product.objects.all().filter(category=category_page,available=True) # ดึงสินค้าพร้อมกับหมวดหมู่
    else :
        products=Product.objects.all().filter(available=True)



    return render(request,'index.html',{'products':products,'category':category_page})
    #Hello Hiblood Donation

def product(request):
    return render(request,'product.html')
