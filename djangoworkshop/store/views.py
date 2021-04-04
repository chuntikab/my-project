# ส่วนของการให้ render ของหน้าเว็บนั้นๆ
from django.shortcuts import render, get_object_or_404, redirect 
from store.models import Category,Product,Cart,CartItem #from django.http import HttpResponse // ตัดออก 9 กพ
from store.forms import SignUpForm
from django.contrib.auth.models import Group,User
from django.contrib.auth.forms import AuthenticationForm #start 1-part36 go to 2-part36(views.py)
from django.contrib.auth import login, authenticate, logout
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def index(request,category_slug=None): # หน้าแรก
    products=None
    category_page=None
    # ถ้าค่า category slug != None
    if category_slug != None: 
        # ทำการค้นหาหมวดหมู่ category
        category_page=get_object_or_404(Category,slug=category_slug)  
        # ดึงสินค้าพร้อมกับหมวดหมู่
        products=Product.objects.all().filter(category=category_page,available=True) 
    else :
        products=Product.objects.all().filter(available=True)

    # set ว่าจะแบ่งสินค้า จำนวน 4 ชิ้น/หน้า 
    # 8 / 3 = 3 page
    paginator=Paginator(products,3)
    # set เลขหน้าเป็นค่าเริ่มต้น
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    # ค่าเริ่มต้นที่กำหนดมา set ให้กับ paginator
    try:
        productperPage=paginator.page(page)
    except(EmptyPage,InvalidPage):
        productperPage=paginator.page(paginator.num_pages)

    return render(request,'index.html',{'products':productperPage,'category':category_page})
    #Hello Hiblood Donation

def productPage(request,category_slug,product_slug): # หน้าสินค้า
    try:
        product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    #แสดงข้อมูลสินค้า พร้อมกับโยนข้อมูลสินค้าที่ดึงมา เอาไปทำงานต่อ
    return render(request,'product.html',{'product':product}) 

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
    # เมื่อไม่พบ object cart
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_id(request))
        # บันทึกลงฐานข้อมูล
        cart.save() 

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
        # ดึงตะกร้า / ตรงนี้มีการฝัง sessions แล้ว
        cart=Cart.objects.get(cart_id=_cart_id(request)) 
        # ดึงข้อมูลสินค้าในตะกร้า
        cart_items=CartItem.objects.filter(cart=cart,active=True) 
        for item in cart_items:
            total += (item.product.price * item.quantity)
            counter += item.quantity 
    except Exception as e:
        pass
    return render(request,'cartdetail.html',dict(cart_items=cart_items,total=total,counter=counter))

def removeCart(request,product_id): # ลบของในตะกร้าสินค้า
    # ทำงานกับตะกร้าสินค้า
    cart=Cart.objects.get(cart_id=_cart_id(request)) # เข้าถึงตะกร้าสินค้าได้แล้ว
    # ทำงานกับสินค้าที่จะลบ  ex product id = 1
    product=get_object_or_404(Product,id=product_id) # เข้าถึงสินค้าได้แล้ว ด้วย product_id
    # เช็คว่ารหัสสินค้าใดเป็น 1 แล้วอยู่ในตะกร้าสินค้าที่กำหนด
    cartItem=CartItem.objects.get(product=product,cart=cart) 
    # ลบรายการสินค้า 1 ออกจากตะกร้า A โดยลบจาก รายการสินค้าในตะกร้า (CartItem)
    cartItem.delete()
    # เมื่อลบเสร็จก็ค้างอยู่ที่หน้าตะกร้าสินค้าเดิม
    return redirect('cartdetail') 

def removeCart(request,product_id): # เอาสินค้าออกจากตะกร้า
    #ทำงานกับตะกร้าสินค้า A
    cart=Cart.objects.get(cart_id=_cart_id(request))
    #ทำงานกับสินค้าที่จะลบ 1
    product=get_object_or_404(Product,id=product_id)
    cartItem=CartItem.objects.get(product=product,cart=cart)
    #ลบรายการสินค้า 1 ออกจากตะกร้า A โดยลบจาก รายการสินค้าในตะกร้า (CartItem)
    cartItem.delete()
    return redirect('cartdetail')

def signUpView(request): # กรณียังไม่มีบัญชี /  ลงทะเบียน 
    #อ้างอิงไปยัง field ที่กำหนด 
    if request.method=='POST': 
        form=SignUpForm(request.POST) 
        #เช็คความถูกต้องของแบบฟอร์ม
        if form.is_valid():
            #บันทึกข้อมูล User ที่โยนมาจากหน้าเว็บ
            form.save() 
            #บันทึก Group Customer
            #ดึง username จากแบบฟอร์มมาใช้
            username=form.cleaned_data.get('username')
            #ดึงข้อมูล user จากฐานข้อมูล
            signUpUser=User.objects.get(username=username)
            #จัด Group โดยไปดึง Group มาทำงานก่อน
            customer_group=Group.objects.get(name="Customer")
            #นำ Group ที่ดึงมาจากฐานข้อมูล กำหนดให้กับ user
            customer_group.user_set.add(signUpUser)
    else :
        form=SignUpForm()
    return render(request,"signup.html",{'form':form}) 

def signInView(request): # กรณีมีบัญชีแล้ว / เข้าใช้ระบบ
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        # เช็คความถูกต้องของข้อม฿ล โดยใช้ตัว Authenticate ของ Django
        if form.is_valid():
            # หากมีการป้อน username , ก็จะรับเข้ามาเก็บที่ตัวแปร username
            username=request.POST['username'] 
            password=request.POST['password']
            # เช็คการยืนยันตัวตนว่าถูกต้องหรือไม่
            user=authenticate(username=username,password=password)
            # ถ้าถูกต้อง...
            if user is not None:
                #ก็ให้ทำการ login และ redirect
                login(request,user)
                return redirect('home')
            # ถ้ายังไม่มี account...
            else:
                return redirect('signUp')
    else:
        form=AuthenticationForm() # from 1-part36,now 2-part36(views.py) go to signin.html(3-part36)
    return render(request,'signIn.html',{'form':form}) # เดิมจาก urls.py(1A)-2A ไปต่อที่ templates-signIn.html(3A) , 

# from urls.py(1B) ไปต่อที่ views.py(2B), now (2B) go to  navbar.html(3B) / part39
def signOutView(request): # ออกจากระบบ
    logout(request)
    return redirect('signIn')

# from urls.py(1C), now is views.py(2C) go to navbar.html(3C)
def serach(request): # ช่อง search
    # ทำการ query ข้อมูล คือวิ่งไปที่ Product / filter ทำการกรองข้อมูลจาก product ตาม name ที่ส่งมา เงื่อนไขคือ ดึงข้อมูลรายการที่มีคำว่า "ex.เสื้อ" แล้วมาเก็บลง object product
    products=Product.objects.filter(name__contains=request.GET['title'])
    # แสดงผลเฉพาะ
    return render(request,'index.html',{'products':products})

