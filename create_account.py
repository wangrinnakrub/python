
# * -------------------------------------- Create Account ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Create_account(QMainWindow):
    switch_to_sign_up = pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setWindowTitle('Create Account')
        self.setGeometry(360, 80, 700, 650) # x,y   w,h
        self.import_style('style_create_account.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.username = ''
        self.password = ''
        self.confirm_password = ''

        self.real_password = ''
        self.real_confirm_password = ''

        self.username_focus = 0
        self.password_focus = 0
        self.confirm_password_focus = 0

        self.active_input_box = None

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mask_last_character)

        self.sign_up_click = 0

        QTimer.singleShot(0, self.clear_initial_focus)
        self.installEventFilter(self)


    # *---------- clear focus ---------- #
    def clear_initial_focus(self):
        self.setFocus(Qt.FocusReason.OtherFocusReason)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if obj not in [self.username_input_box, self.password_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.username_input_box.clearFocus()
        self.password_input_box.clearFocus()
        self.setFocus(Qt.FocusReason.OtherFocusReason)


    # *---------- import style from qss ---------- #
    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")


    # *---------- layout ---------- #
    def ui(self):
        self.layout = QVBoxLayout()
        self.addWidgetsToLayout(self.layout)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)


    # *---------- create account page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to sign up -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        # self.back_button.setIcon(QIcon("C:\pic\go-back.png"))
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_up')
        self.back_button.clicked.connect(self.switch_to_sign_up.emit)
        ui.addWidget(self.back_button)

        ui.addStretch()
        # *----------- create account ----------- #
        # create account label
        self.create_account_label = QLabel('Create Account')
        self.create_account_label.setObjectName('create_account_label')
        self.create_account_label.setFixedHeight(100)

        # create account layout
        create_account_layout = QHBoxLayout()
        create_account_layout.addStretch()
        create_account_layout.addWidget(self.create_account_label)
        create_account_layout.addStretch()
        ui.addLayout(create_account_layout)


        # *----------- Username ----------- #
        # username label
        self.username_label = QLabel('Username')
        self.username_label.setObjectName('username_label')
        self.username_label.setFixedSize(350,50)

        # username label layout
        username_layout = QHBoxLayout()
        username_layout.addStretch()
        username_layout.addWidget(self.username_label)
        username_layout.addStretch()
        ui.addLayout(username_layout)

        # username input box
        self.username_input_box = QLineEdit()
        self.username_input_box.setObjectName('username_input_box')
        self.username_input_box.setPlaceholderText('Type your username')
        self.username_input_box.returnPressed.connect(self.username_enter)
        self.username_input_box.setFixedSize(305, 40)

        # username input box layout
        username_input_box_layout = QHBoxLayout()
        username_input_box_layout.setObjectName('username_input_box_layout')
        username_input_box_layout.addStretch()
        username_input_box_layout.addWidget(self.username_input_box)
        username_input_box_layout.addStretch()
        ui.addLayout(username_input_box_layout)

        # todo username error label
        self.username_error_label = QLabel('')
        self.username_error_label.setObjectName('username_error_label')
        self.username_error_label.setFixedHeight(20)

        # todo username error label layout
        username_error_label_layout = QHBoxLayout()
        username_error_label_layout.setObjectName('username_error_label_layout')
        username_error_label_layout.addStretch()
        username_error_label_layout.addWidget(self.username_error_label)
        username_error_label_layout.addStretch()
        ui.addLayout(username_error_label_layout)


        # *----------- Password ----------- #
        # password label
        self.password_label = QLabel('Password')
        self.password_label.setObjectName('password_label')
        self.password_label.setFixedSize(350,50)

        # password label layout
        password_layout = QHBoxLayout()
        password_layout.addStretch()
        password_layout.addWidget(self.password_label)
        password_layout.addStretch()
        ui.addLayout(password_layout)

        # password input box
        self.password_input_box = QLineEdit()
        self.password_input_box.setObjectName('password_input_box')
        self.password_input_box.setPlaceholderText('Type your password')
        self.password_input_box.returnPressed.connect(self.password_enter)
        self.password_input_box.textChanged.connect(lambda: self.handle_text_change(self.password_input_box, self.password_input_box.text(), is_password=True))
        self.password_input_box.setFixedSize(305, 40)

        # password input box layout
        password_input_box_layout = QHBoxLayout()
        password_input_box_layout.setObjectName('password_input_box_layout')
        password_input_box_layout.addStretch()
        password_input_box_layout.addWidget(self.password_input_box)
        password_input_box_layout.addStretch()
        ui.addLayout(password_input_box_layout)
        self.previous_text = ''

        # todo password error label
        self.password_error_label = QLabel('')
        self.password_error_label.setObjectName('password_error_label')
        self.password_error_label.setFixedHeight(20)

        # todo password error label layout
        password_error_label_layout = QHBoxLayout()
        password_error_label_layout.setObjectName('password_error_label_layout')
        password_error_label_layout.addStretch()
        password_error_label_layout.addWidget(self.password_error_label)
        password_error_label_layout.addStretch()
        ui.addLayout(password_error_label_layout)


        # *----------- Confirm_password ----------- #
        # confirm_password label
        self.confirm_password_label = QLabel('Confirm Password')
        self.confirm_password_label.setObjectName('confirm_password_label')
        self.confirm_password_label.setFixedSize(350,50)

        # confirm_password label layout
        confirm_password_label_layout = QHBoxLayout()
        confirm_password_label_layout.addStretch()
        confirm_password_label_layout.addWidget(self.confirm_password_label)
        confirm_password_label_layout.addStretch()
        ui.addLayout(confirm_password_label_layout)

        # confirm_password input box
        self.confirm_password_input_box = QLineEdit()
        self.confirm_password_input_box.setObjectName('confirm_password_input_box')
        self.confirm_password_input_box.setPlaceholderText('Type your confirm password')
        self.confirm_password_input_box.returnPressed.connect(self.confirm_password_enter)
        self.confirm_password_input_box.textChanged.connect(lambda: self.handle_text_change(self.confirm_password_input_box, self.confirm_password_input_box.text(), is_password=False))
        self.confirm_password_input_box.setFixedSize(305,50)
        self.previous_confirm_password = ''

        # confirm_password input box layout
        confirm_password_input_box_layout = QHBoxLayout()
        confirm_password_input_box_layout.setObjectName('confirm_password_input_box_layout')
        confirm_password_input_box_layout.addStretch()
        confirm_password_input_box_layout.addWidget(self.confirm_password_input_box)
        confirm_password_input_box_layout.addStretch()
        ui.addLayout(confirm_password_input_box_layout)

        # todo Confirm_password error label
        self.confirm_password_error_label = QLabel('')
        self.confirm_password_error_label.setObjectName('confirm_password_error_label')
        self.confirm_password_error_label.setFixedHeight(20)

        # todo confirm_password error label layout
        confirm_password_error_label_layout = QHBoxLayout()
        confirm_password_error_label_layout.setObjectName('confirm_password_error_label_layout')
        confirm_password_error_label_layout.addStretch()
        confirm_password_error_label_layout.addWidget(self.confirm_password_error_label)
        confirm_password_error_label_layout.addStretch()
        ui.addLayout(confirm_password_error_label_layout)

        ui.addSpacing(25)


        # *---------- Create account button ----------- #
        # sign_up button
        self.create_account_button = QPushButton('Create Account')
        self.create_account_button.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #43d9ff, stop:1 #ff56c7);')
        self.create_account_button.setObjectName('create_account_button')
        self.create_account_button.setFixedSize(230,37)
        self.create_account_button.clicked.connect(self.create_account_clicked)

        # create_account button layout
        create_account_button_layout = QHBoxLayout()
        create_account_button_layout.setObjectName('create_account_button_layout')
        create_account_button_layout.setContentsMargins(0,10,0,65)
        create_account_button_layout.addStretch()
        create_account_button_layout.addWidget(self.create_account_button)
        create_account_button_layout.addStretch()
        ui.addLayout(create_account_button_layout)

        ui.addStretch()

    # * -------------------- password to ● -------------------- * #
    def handle_text_change(self, input_box, text, is_password=True):
        if self.timer.isActive():
            self.timer.stop()

        self.active_input_box = input_box

        if is_password:
            # อัปเดต real_password ตามที่พิมพ์ โดยไม่ mask
            self.real_password = text

            if len(text) > len(self.previous_text):
                masked_password = '●' * (len(text) - 1) + text[-1]
            else:
                masked_password = '●' * len(text)

            self.previous_text = text
            input_box.blockSignals(True)
            input_box.setText(masked_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_password))

        else:
            # อัปเดต real_confirm_password ตามที่พิมพ์ โดยไม่ mask
            self.real_confirm_password = text

            if len(text) > len(self.previous_confirm_password):
                masked_confirm_password = '●' * (len(text) - 1) + text[-1]
            else:
                masked_confirm_password = '●' * len(text)

            self.previous_confirm_password = text
            input_box.blockSignals(True)
            input_box.setText(masked_confirm_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_confirm_password))

        self.timer.start(700)

    # *---------- mask last character after timeout ---------- #

    def mask_last_character(self):
        self.timer.stop()
        if self.active_input_box is not None:
            if self.active_input_box == self.password_input_box:
                masked_password = '●' * len(self.real_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_password))

            elif self.active_input_box == self.confirm_password_input_box:
                masked_confirm_password = '●' * len(self.real_confirm_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_confirm_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_confirm_password))


    # *---------- check username enter ---------- #
    def username_enter(self):
        self.username_focus += 1
        if self.username_focus >= 1:
            self.check_create_account()

        self.username = self.username_input_box.text()
        if self.username != '':
            self.password_input_box.setFocus()

    # *---------- check password enter ---------- #
    def password_enter(self):
        self.password_focus += 1
        if self.password_focus >= 1:
            self.check_create_account()

        self.password = self.password_input_box.text()
        if self.password != '':
            self.confirm_password_input_box.setFocus()

    # *---------- check confirm password enter ---------- #
    def confirm_password_enter(self):
        self.confirm_password_focus += 1
        if self.confirm_password_focus >= 1:
            self.check_create_account()

    # *---------- check create account clicked ---------- #
    def create_account_clicked(self):
        self.password = self.password_input_box.text()
        self.confirm_password = self.confirm_password_input_box.text()

        if self.password == '':
            self.password_enter()
        elif self.confirm_password == '':
            self.confirm_password_enter()
        else:
            self.check_create_account()



    # *---------- check create account ---------- #
    def check_create_account(self):
        self.username = self.username_input_box.text()
        valid = True

        if self.username == '':
            self.username_error_label.setText('Please enter your username')
            self.password_error_label.setText('')
            self.confirm_password_error_label.setText('')

        elif self.password == '':
            self.username_error_label.setText('')
            self.confirm_password_error_label.setText('')
            if self.password_focus >= 1:
                self.password_error_label.setText('Please enter your password')

        elif self.confirm_password == '':
            self.username_error_label.setText('')
            self.password_error_label.setText('')
            if self.confirm_password_focus >= 1:
                self.confirm_password_error_label.setText('Please enter your confirm password')


        if self.username != '':
            self.username_error_label.setText('')

        if self.password != '':
            self.password_error_label.setText('')

        if self.real_confirm_password != '':
            if self.real_confirm_password != self.real_password:
                self.confirm_password_error_label.setText('Password does not match')
            else:
                self.confirm_password_error_label.setText('')
                # self.open_main_window()


    # # *---------- back to sign up ----------* #
    # def back_to_signup_page(self):
    #     from sign_up import Signup_page
    #     self.sign_up_page = Signup_page()
    #     self.sign_up_page.show()
    #     self.close()

    # # *---------- open main window ----------* #
    # def open_main_window(self):
    #     from main_window import MainWindow
    #     self.main_window = MainWindow()
    #     self.main_window.show()
    #     self.close()


#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    create_account = Create_account()
    # Create_account.showMaximized()
    create_account.show()
    app.exec()
