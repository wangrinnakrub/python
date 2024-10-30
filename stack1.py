from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys

from sign_in import Signin_page
from sign_up import Signup_page
from create_account import Create_account
from forgot_password import Forgot_password_page
from reset_password import Reset_password
from main_window import MainWindow


class MainApp(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Basketball Score Sheet')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.sign_in = Signin_page()
        self.sign_up = Signup_page()
        self.create_account = Create_account()
        self.forgot_password = Forgot_password_page()
        self.reset_password = Reset_password()
        self.main_window = MainWindow()

        # Add widgets to stack
        self.addWidget(self.sign_in)
        self.addWidget(self.sign_up)
        self.addWidget(self.create_account)
        self.addWidget(self.forgot_password)
        self.addWidget(self.reset_password)
        self.addWidget(self.main_window)

        self.setCurrentWidget(self.sign_in)
        self.setGeometry(360, 110, 700, 650)

        # sign in
        self.sign_in.switch_to_forgot_password.connect(lambda: self.switch_with_animation_from_right(self.forgot_password))
        self.sign_in.switch_to_main_window.connect(lambda: self.switch_with_animation_from_right(self.main_window))
        self.sign_in.switch_to_sign_up.connect(lambda: self.switch_with_animation_from_right(self.sign_up))

        # sign up
        self.sign_up.switch_to_sign_in.connect(lambda: self.switch_with_animation_from_left(self.sign_in))
        self.sign_up.switch_to_create_account.connect(lambda: self.switch_with_animation_from_right(self.create_account))

        # forgot password
        self.forgot_password.switch_to_sign_in.connect(lambda: self.switch_with_animation_from_left(self.sign_in))
        self.forgot_password.switch_to_reset_passsword.connect(lambda: self.switch_with_animation_from_right(self.reset_password))

        # create account
        self.create_account.switch_to_sign_up.connect(lambda: self.switch_with_animation_from_left(self.sign_up))


        self.animation = None

    def switch_with_animation_from_right(self, new_widget):
        new_widget.setGeometry(self.width(), 0, self.width(), self.height())

        self.setCurrentWidget(new_widget)

        self.animation = QPropertyAnimation(new_widget, b"pos")
        self.animation.setDuration(300)
        self.animation.setStartValue(QPoint(self.width(), 0))
        self.animation.setEndValue(QPoint(0, 0))
        self.animation.start()


    def switch_with_animation_from_left(self, new_widget):
        # ตั้งค่าตำแหน่งเริ่มต้นสำหรับ widget ใหม่ (เลื่อนเข้ามาจากทางซ้าย)
        new_widget.setGeometry(-self.width(), 0, self.width(), self.height())  # เริ่มจากด้านซ้าย

        # เปลี่ยน widget ใหม่เป็น widget ปัจจุบัน
        self.setCurrentWidget(new_widget)

        # สร้างแอนิเมชันสำหรับเลื่อนเข้ามาของ widget
        self.animation = QPropertyAnimation(new_widget, b"pos")
        self.animation.setDuration(300)  # ระยะเวลาแอนิเมชันเป็นมิลลิวินาที
        self.animation.setStartValue(QPoint(-self.width(), 0))  # เริ่มจากตำแหน่งนอกซ้าย
        self.animation.setEndValue(QPoint(0, 0))  # สิ้นสุดที่ตำแหน่งปกติ
        self.animation.start()


app = QApplication(sys.argv)
main_app = MainApp()
main_app.show()
sys.exit(app.exec())

