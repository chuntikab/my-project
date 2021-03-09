from django.shortcuts import render, get_object_or_404, redirect # ส่วนของการให้ render ของหน้าเว็บนั้นๆ
from store.models import Category,Product,Cart,CartItem #from django.http import HttpResponse // ตัดออก 9 กพ

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

def productPage(request,category_slug,product_slug): # หน้าสินค้า
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product}) #แสดงข้อมูลสินค้า พร้อมกับโยนข้อมูลสินค้าที่ดึงมา เอาไปทำงานต่อ

def _cart_id(request): # sessions ฝังข้อมูลการสั่งซื้อไม่ให้หายบนเครื่อง client
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def addCart(request,product_id):
    # รหัสสินค้า
    # ดึงสินค้าตามรหัสที่ส่งมา
    product=Product.objects.get(id=product_id)

    # สร้างตะกร้าสินค้า
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist: # เมื่อไม่พบ object cart
        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save() # บันทึกลงฐานข้อมูล

    # เมื่อมีตะกร้าสินค้าแล้ว
    try:
        # ซื้อรายการสินค้าซ้ำ
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            # เปลี่ยนจำนวน quantity
            cart_item.quantity += 1
            # บันทึก / อัพเดทค่า
            cart_item.save()
    except CartItem.DoesNotExist:
        # ซื้อรายการสินค้าครั้งแรก
        # บันทึกลงฐานข้อมูล
        cart_item=CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()
    return redirect('/')
        
def cartdetail(request): # หน้าตะกร้าสินค้า
    total=0 # ราคาทั้งหมด
    counter=0 # จำนวนสินค้าในตะกร้า
    cart_item=None # รายการสินค้าแต่ละรายการ ที่ได้จากการ loop
    # ดึงข้อมูลจากฐานข้อมูล
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request)) # ดึงตะกร้า / ตรงนี้มีการฝัง sessions แล้ว
        cart_items=CartItem.objects.filter(cart=cart,active=True) # ดึงข้อมูลสินค้าในตะกร้า
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity 
    except Exception as e:
        pass
    return render(request,'cartdetail.html',dict(cart_items=cart_items,total=total,counter=counter))
