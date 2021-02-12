import requests
import json

base = input("แปลงจากสกุลเงิน : ") #หน่วยสกุลเงิน
to = input("เป็นสกุลเงิน : ")  #หน่วยสกุลเงิน
amount = float(input("จำนวนเงิน : ")) 


url = "https://api.exchangeratesapi.io/latest?base="+base


response = requests.get(url)
data = response.text
parsed  =json.loads(data)
rates = parsed["rates"]

#loop ข้อมูล
for currency,rate in rates.items(): #เปรียบเทียบ
    if currency == to:
        conversion = rate*amount #คำนวณหาจำนวนเงินที่เทียบ
        print("1",base,"=",currency,rate)
        print(amount,base,"=",currency,conversion)

