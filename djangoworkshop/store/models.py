# ส่วนของการ สร้างตาราง DB
from django.db import models
from django.urls import reverse

# Create your models here.

# หมวดหมู่
class Category(models.Model): 
    name=models.CharField(max_length=255,unique=True) #ข้อมูลเป็นตัวอักษรขนาดไม่เกิน 255 แบบห้ามซ้ำกัน หรือ unique (auto increament)
    slug=models.SlugField(max_length=255,unique=True) #slug เป็นการตั้งชื่อเล่นให้ข้อมูลในโมเดล #generate url ไปกับชื่อสินค้า

    #แปลง object ให้เป็น str
    def __str__(self):
        return self.name

    class Meta : # เปลี่ยนให้เป็นชื่อภาษาไทย 
        ordering=('name',) # ใช้ในการ sort เช่น sort ตาม name
        verbose_name='หมวดหมู่สินค้า'
        verbose_name_plural="ข้อมูลประเภทสินค้า"
        # สาเหตุที่ต้อง ระบุ class Meta เพราะใน DB เราต้องตั้งชื่อฐานข้อมูล ชื่อตารางเป็น Eng การทำ class Meta ช่วยให้ทำงานง่ายชึ้น

    def get_url(self): 
        return reverse('product_by_category',args=[self.slug]) # ....

# สินค้า
class Product(models.Model): 
    name=models.CharField(max_length=255,unique=True) #ชื่อ
    slug=models.SlugField(max_length=255,unique=True) 
    description=models.TextField(blank=True) #รายละเอียด
    price=models.DecimalField(max_digits=10,decimal_places=2) #ราคา !!!!!!!!!!!!!!!!!!!
    category=models.ForeignKey(Category,on_delete=models.CASCADE) #ลบข้อมูลที่มีความสัมพันธ์กันระหว่าง 2 ตาราง กรณีที่มีความสัมพันธ์กัน เช่น ลบหมวดหมู่ + ลบสินค้า
    image=models.ImageField(upload_to="product",blank=True) #upload ภาพสินค้า ไปยัง Folder "product"
    stock=models.IntegerField()
    available=models.BooleanField(default=True) #สถานะของสินค้า เช่น สินค้ามีปัญหา ก็ไม่ต้องเก็ยที่หน้าเว็บ
    created=models.DateTimeField(auto_now_add=True) #วันที่บันทึกข้อมูลสินค้า ณ ปัจจุบันที่บันทึกเลย
    updated=models.DateTimeField(auto_now=True) #ข้อมูลวัน ณ ปัจจุบันที่ทำงานอยู่

    def __str__(self):
        return self.name

    class Meta :
        ordering=('name',) # ใช้ในการ sort เช่น sort ตาม name
        # เปลี่ยนให้เป็นชื่อภาษาไทย
        verbose_name='สินค้า'
        verbose_name_plural="ข้อมูลสินค้า"

    def get_url(self): 
        return reverse('productDetail',args=[self.category.slug,self.slug]) # ....

# ตะกร้าสินค้า / มีการนำคุณสมบัติ models มาใช้
class Cart(models.Model): 
    cart_id=models.CharField(max_length=255,blank=True) # เป็นค่าว่างได้
    date_added=models.DateTimeField(auto_now_add=True) # เก็บวันเวลาที่สร้างตะกร้าสินค้า/วันที่ผู้ใช้บริการหยิบสินค้าลงตะกร้า

    # เปลี่ยนตัว obj ให้เป็น str
    def __str__(self):
        return self.cart_id

    class Meta:
        db_table='cart'
        ordering=('date_added',)
        # เปลี่ยนให้เป็นชื่อภาษาไทย
        verbose_name='ตะกร้าสินค้า'
        verbose_name_plural="ข้อมูลตะกร้าสินค้า"

# รายการสินค้าในตะกร้า / โยงข้อมูลกับ2โมเดล คือ โมเดลตะกร้าสินค้าที่ใช้จัดเก้บ และ โมเดลสินค้า
class CartItem(models.Model): 
    product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE) 
    quantity=models.IntegerField() # จำนวนรายการสินค้าที่เพิ่มลงตะกร้า
    active=models.BooleanField(default=True) # 

    class Meta:
        db_table='cartItem'
        #ordering=('date_added',)
        # เปลี่ยนให้เป็นชื่อภาษาไทย
        verbose_name='รายการสินค้าในตะกร้า'
        verbose_name_plural="ข้อมูลรายการสินค้าในตะกร้า"

    # ฟังก์ชันในการคำนวนหาผลรวม
    def sub_total(self): 
        return self.product.price * self.quantity # <!-- แก้ราคา @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ใส่เป็นแต้มคะแนน*******************************-->

    # เปลี่ยนตัว obj ให้เป็น str
    def __str__(self):
        return self.product.name

# ใบสั่งซื้อ
class Order(models.Model):
    # 1 เก็บชื่อลูกค้า
    name=models.CharField(max_length=255,blank=True)
    # 2 ที่อยู่
    address=models.CharField(max_length=255,blank=True)
    # 3 เมือง
    city=models.CharField(max_length=255,blank=True)
    # 4 รหัสไปรษณีย์
    postcode=models.CharField(max_length=255,blank=True)
    # 5 ยอดที่ต้องชำระ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ แต้มที่ต้องแลกทั้งหมด
    total=models.DecimalField(max_digits=10,decimal_places=2)
    # 6 email
    email=models.EmailField(max_length=250,blank=True)
    # 7 token / ถูกโยนเมื่อมีการใช้ API ชำระเงิน
    token=models.CharField(max_length=255,blank=True)

    # DB : สร้างตาราง
    class Meta:
        # ตารางชื่อว่า Order
        db_table='Order' 
    # การแสดงผล
    def __str__(self):
        return str(self.id)

# รายการสินค้าภายในใบสั่งซื้อ
# โมเดลที่ผูกกับ โมเดลorder
class OrderItem(models.Model):
    # 1 ชื่อสินค้านั้น 
    product=models.CharField(max_length=250)
    # 2 จำนวน
    quantity=models.IntegerField()
    # 3 ราคา @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ แต้ม
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # 4 อ้างอิงไปใบสั่งซืิ้อ
    order=models.ForeignKey(Order,on_delete=models.CASCADE)

    # DB : สร้างตาราง
    class Meta:
        db_table='OrderItem'

    # ยอดรวมของสินค้าแต่ละรายการ
    def sub_total(self):
        return self.quantity * self.price

    # การแสดงข้อมูลของสินค้า ในส่วนของ Admin Dashboard
    def __str__(self):
        return self.product







