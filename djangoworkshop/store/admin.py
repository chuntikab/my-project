# class การทำงานของ Admin Dashboard
from django.contrib import admin # ลงทะเบียนหรืออัพข้อมูลขึ้น db และ แสดงส่วน admin dashboard ด้วย
from store.models import Category,Product,Cart,CartItem,Order,OrderItem,Userpoint

# Register your models here.

# ปรับแต่ง Product Admin / ทำการแสดงข้อมูลของสินค้า โดยไม่ต้องคลิกเข้าไปสินค้านั้นก็ได้
class ProductAdmin(admin.ModelAdmin):
    # ดูได้จาก ฐานข้อมูลใน sql
    list_display=['name','price','stock','created','updated'] 
    # ทำให้สามรถแก้ไขขอ้มูล ได้ที่หน้านั้นเลย โดยไม่ต้องกดเข้าในสินค้า
    list_editable=['price','stock']
    # ดูได้จาก ฐานข้อมูลใน sql
    list_per_page=5

class OrderAdmin(admin.ModelAdmin):
    # ดูได้จาก ฐานข้อมูลใน sql
    list_display=['id','name','email','total','token','created','updated'] 
    list_per_page=5

class OrderItemAdmin(admin.ModelAdmin):
    # ดูได้จาก ฐานข้อมูลใน sql
    list_display=['order','product','quantity','price','created','updated'] 
    list_per_page=5

class UserPointsAdmin(admin.ModelAdmin):
    # ดูได้จาก ฐานข้อมูลใน sql
    list_display=['name','totalp'] 
    list_per_page=5

admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Userpoint,UserPointsAdmin)