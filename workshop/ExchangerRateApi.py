import requests
import json
response=requests.get('https://api.exchangeratesapi.io/latest')
data=response.text

parsed=json.loads(data)
#print(json.dumps(parsed,indent=4)) #แสดงข้อมูลทั้งหมด

date=parsed["date"] #ดึงข้อมูลวันที่
#print(date)

usd_rate=parsed["rates"]["USD"] #ดึงข้อมูลสกุลเงินที่ต้องการรู้
thb_rate=parsed["rates"]["THB"]
print("1 EUR = "+str(usd_rate)+" USD")
print("1 EUR = "+str(thb_rate)+" THB")

