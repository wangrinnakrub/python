
import re

def is_valid_email(email):
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email) is not None

def check_email_syntax(email):
    return is_valid_email(email)





# import re

# def is_valid_email(email):
#     # รูปแบบ regex สำหรับตรวจสอบอีเมล
#     email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
#     return re.match(email_regex, email) is not None

# # ตัวอย่างการใช้งาน
# def check_email_syntax(email):
#     valid = False
#     if is_valid_email(email):
#         valid = True
#     else:
#         valid = False

#     return valid
