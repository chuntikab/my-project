from django.contrib import admin # ลงทะเบียน หรือ อัพข้อมูลขึ้น db และแสดงส่วน admin dashboard ด้วย
from store.models import Category,Product,Cart,CartItem


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)

