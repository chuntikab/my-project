import tkinter as tk
import requests
import json

def show_output():

    #amount= float(amount_input.get())

    output1=''
    output2=''
    
    for currency,rate in rates.items(): #เปรียบเทียบ
        if currency == to:
            conversion = rate*amount #คำนวณหาจำนวนเงินที่เทียบ
            output1="1",base,"=",currency,rate
            output2=amount,base,"=",currency,conversion
            print("1",base,"=",currency,rate)
            print(amount,base,"=",currency,conversion)
            output_label1.configure(text=output1)
            output_label2.configure(text=output2)
            output_label3.configure(text=output3)






#base = str("แปลงจากสกุลเงิน : ") #หน่วยสกุลเงิน
#to = str("เป็นสกุลเงิน : ")  #หน่วยสกุลเงิน
#amount = float(input("จำนวนเงิน : "))

base = input("แปลงจากสกุลเงิน : ") #หน่วยสกุลเงิน
to = input("เป็นสกุลเงิน : ")  #หน่วยสกุลเงิน
amount = float(input("จำนวนเงิน : ")) 

url = "https://api.exchangeratesapi.io/latest?base="+base


response = requests.get(url)
data = response.text
parsed  =json.loads(data)
rates = parsed["rates"]

date=parsed["date"] #ดึงข้อมูลวันที่
#print(date)
output3=date

window = tk.Tk()
window.title('อัตราแลกเปลี่ยนสกุลเงิน')
window.minsize(width = 400, height=400)

title_label = tk.Label(master = window, text = "แปลงจากสกุลเงิน")
title_label.pack()

base = tk.Entry(master=window)
base_2 = str(base)
base.pack()

title_label2 = tk.Label(master = window, text = "เป็นสกุลเงิน")
title_label2.pack()

to = tk.Entry(master=window)
to.pack()

title_label3 = tk.Label(master = window, text = "จำนวนเงิน")
title_label3.pack()

amount_input = tk.Entry(master=window)
amount_input.pack()

go_button = tk.Button(
    master=window, text='แปลงจำนวนเงิน',
    command = show_output
)
go_button.pack()

output_label1 = tk.Label(master=window)
output_label1.pack()
output_label2 = tk.Label(master=window)
output_label2.pack()
output_label3 = tk.Label(master=window)
output_label3.pack()


window.mainloop()