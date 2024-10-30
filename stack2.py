# testt

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QPropertyAnimation, QRect
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

        # Start with the sign-in page
        self.setCurrentWidget(self.sign_in)
        self.setGeometry(360, 110, 700, 650)

        # Connect signals to switch pages with animations
        self.sign_in.switch_to_forgot_password.connect(lambda: self.switch_with_animation(self.forgot_password))
        self.sign_in.switch_to_main_window.connect(lambda: self.switch_with_animation(self.main_window))
        self.sign_in.switch_to_sign_up.connect(lambda: self.switch_with_animation(self.sign_up))
        self.sign_up.switch_to_sign_in.connect(lambda: self.switch_with_animation(self.sign_in))
        self.sign_up.switch_to_create_account.connect(lambda: self.switch_with_animation(self.create_account))

    def switch_with_animation(self, new_widget):
        current_widget = self.currentWidget()
        

        # Set the initial size of the new widget to be small and centered
        center_x = (self.width() - 50) // 2
        center_y = (self.height() - 50) // 2
        new_widget.setGeometry(center_x, center_y, 50, 50)  # Start small

        # Create an animation for expanding the new widget first in Y and then in X
        self.animation_y = QPropertyAnimation(new_widget, b"geometry")
        self.animation_y.setDuration(300)
        self.animation_y.setStartValue(QRect(center_x, center_y, 0, 10))  # Start small
        self.animation_y.setEndValue(QRect(center_x, 0, 10, self.height()))  # Expand to full height

        # Start the Y expansion animation
        self.animation_y.start()

        # Connect to the finished signal to start the X expansion animation
        self.animation_y.finished.connect(lambda: self.expand_x(new_widget, center_x))

        # Change the current widget to the new widget
        self.setCurrentWidget(new_widget)

    def expand_x(self, new_widget, center_x):
        # Create an animation for expanding the new widget in X direction
        self.animation_x = QPropertyAnimation(new_widget, b"geometry")
        self.animation_x.setDuration(300)
        self.animation_x.setStartValue(new_widget.geometry())  # Start from current size
        self.animation_x.setEndValue(QRect(0, 0, self.width(), self.height()))  # Expand to full size
        self.animation_x.start()


app = QApplication(sys.argv)
main_app = MainApp()
main_app.show()
sys.exit(app.exec())
