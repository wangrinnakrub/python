import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_otp(length=6):
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

def send_otp_via_email(receiver_email, otp):
    sender_email = 'basketballscoresheet.official@gmail.com'
    sender_password = 'akmg zmum nerj iftq'

    # สร้างข้อความอีเมล
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Your OTP code from Basketball Score Sheet'
    # message['Subject'] = 'เลขเด็ด'

    body = f'Your OTP code is {otp}'
    # body = f'มาส่งเลขเด็ดครับ {otp}'
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f'OTP sent to {receiver_email}')
        server.quit()
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    receiver_email = 'kantaphit17@gmail.com'
    otp = generate_otp()
    print(f'Generated OTP: {otp}')
    send_otp_via_email(receiver_email, otp)



# ! ------------------------------------------------------------------------------------------

# import smtplib
# import random
# import time
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # กำหนดระยะเวลาให้ OTP ใช้งาน (5 นาที)
# OTP_VALIDITY_DURATION = 300  # 300 วินาที (5 นาที)

# def generate_otp(length=6):
#     otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
#     return otp

# def send_otp_via_email(receiver_email, otp):
#     sender_email = 'basketballscoresheet.official@gmail.com'
#     sender_password = 'akmg zmum nerj iftq'

#     # สร้างข้อความอีเมล
#     message = MIMEMultipart()
#     message['From'] = sender_email
#     message['To'] = receiver_email
#     message['Subject'] = 'Your OTP code from Basketball Score Sheet'

#     body = f'เอา otp ไปซะ นี่แหนะ {otp}'
#     message.attach(MIMEText(body, 'plain'))

#     try:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)

#         server.sendmail(sender_email, receiver_email, message.as_string())
#         print(f'OTP sent to {receiver_email}')
#         server.quit()
#     except Exception as e:
#         print(f'Error: {e}')

# def is_otp_valid(otp_creation_time):
#     current_time = time.time()
#     return (current_time - otp_creation_time) <= OTP_VALIDITY_DURATION

# if __name__ == "__main__":
#     receiver_email = 'kantaphit1@gmail.com'
#     otp = generate_otp()  # สุ่มรหัส OTP
#     otp_creation_time = time.time()  # เวลาที่รหัส OTP ถูกสร้าง
#     print(f'Generated OTP: {otp}')

#     # ส่ง OTP ผ่านอีเมล
#     send_otp_via_email(receiver_email, otp)

#     # ทดสอบการตรวจสอบ OTP หลังจากเวลาผ่านไป (สามารถเพิ่มการสอบถามผู้ใช้ที่นี่)
#     time.sleep(10)  # หยุดการทำงาน 10 วินาที เพื่อจำลองการรอ
#     if is_otp_valid(otp_creation_time):
#         print("OTP is still valid.")
#     else:
#         print("OTP has expired.")
