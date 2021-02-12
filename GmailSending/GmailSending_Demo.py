#ธัญธิชา หาญศิริสถาพร 6010450349
#ฉันทิกา บำรุง 6010451027
import smtplib
import Config

recipient=input("ป้อนอีเมลผู้รับ: ")
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(Config.email,Config.password)

content="hi"
subject="Test project Protocol"

email_text="""
From:%s
To:%s
subject:%s
%s
"""%(Config.email,recipient,subject,content)

server.sendmail(Config.email,recipient,email_text)
server.quit
print("Send Complete")
