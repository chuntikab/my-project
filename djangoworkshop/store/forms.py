# class โครงสร้าง-ดำเนินการเกี่ยวกับ แบบฟอร์มลงทะเบียน และ ตัวmodel user
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm # เป็นการบอกว่าเราจะสร้าง user ขึ้นมาผ่าน แบบฟอร์ม // data binding

#ออกแบบ column ในฐานข้อมูล
class SignUpForm(UserCreationForm): ##ออกแบบ แบบฟอร์ม โดยใช้ฟอร์มของ Django 
    first_name=forms.CharField(max_length=100,required=True) # เสมือนว่า ในตัว Textfield firstname ที่ปรากฎอยู่ในหน้าเว็บเนี่ย รองรับตัวอักษรได้ 100 ตัว และบังคับให้ป้อนข้อมูลนี้ทุกครั้งที่ลงทะเเบียน
    last_name=forms.CharField(max_length=100,required=True) # เสมือนว่า ในตัว Textfield lastname ที่ปรากฎอยู่ในหน้าเว็บเนี่ย รองรับตัวอักษรได้ 100 ตัว และบังคับให้ป้อนข้อมูลนี้ทุกครั้งที่ลงทะเเบียน
    email=forms.EmailField(max_length=250,help_text='example@gmail.com')

    class Meta: #ระบุ เพื่อที่จะให้สิ่งนี้ทำงานที่ model อะไร // ซึ่งก็คือ model user
        model=User #model ในตารางฐานข้อมูล
        fields=('first_name','last_name','username','email','password1','password2') #Tuple / ผูกข้อมูลที่model user,ระบุ feild / เป็นการกำหนดส่วนที่จะให้ลูกคค้ากรอก และ เป็นการ validate ข้อมูลด้วย