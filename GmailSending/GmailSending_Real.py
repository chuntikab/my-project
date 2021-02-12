#ธัญธิชา หาญศิริสถาพร 6010450349
#ฉันทิกา บำรุง 6010451027
import smtplib, ssl
import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "conannewz1007@gmail.com"  # อีเมลผู้ส่ง
receiver_email = "chuntika.b@ku.th"  # อีเมลผู้รับ
password = getpass.getpass("Enter your password: ")

message = """\
Subject: protocol project 

This message is sent from my protocol project.

Hello , my name is Chuntika Bumrung 

id student: 6010451027"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

server.quit
print("Send Complete")