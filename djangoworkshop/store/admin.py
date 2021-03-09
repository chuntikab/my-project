from django.contrib import admin # ลงทะเบียน หรือ อัพขอมูลขึ้น db และแสดงส่วน admin dashboard ด้วย
from store.models import Category,Product


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)

