from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model): # หมวดหมู่
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

class Product(models.Model): # สินค้า
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

    class Meta : # เปลี่ยนให้เป็นชื่อภาษาไทย
        ordering=('name',) # ใช้ในการ sort เช่น sort ตาม name
        verbose_name='สินค้า'
        verbose_name_plural="ข้อมูลสินค้า"






