
# * -------------------------------------- Reset_password ----------------------------------------- #

# ------------------ import libary ------------------ #
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Reset_password(QMainWindow):
    switch_to_forgot_password =  pyqtSignal()
    switch_to_main_window = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Reset_password')
        self.setGeometry(360, 80, 700, 650) # x,y   w,h
        self.import_style('style_reset_password.qss')
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.ui()

        self.new_password = ''
        self.confirm_new_password = ''

        self.real_new_password = ''
        self.real_confirm_new_password = ''

        self.new_password_focus = 0
        self.confirm_new_password_focus = 0

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
            if obj not in [self.new_password_input_box, self.confirm_new_password_input_box]:
                self.clear_focus_from_all()
        return super().eventFilter(obj, event)

    def clear_focus_from_all(self):
        self.new_password_input_box.clearFocus()
        self.confirm_new_password_input_box.clearFocus()
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


    # *---------- reset_password page widget ---------- #
    def addWidgetsToLayout(self, ui):

        # *------- back to sign up -------* #
        self.back_button = QPushButton()
        self.back_button.setFixedSize(40, 40)
        # self.back_button.setIcon(QIcon("C:\pic\go-back.png"))
        self.back_button.setIcon(QIcon("C:\pic\—Pngtree—vector back icon_4267356.png"))
        self.back_button.setIconSize(QSize(25,25))
        self.back_button.setContentsMargins(20,20,0,0)
        self.back_button.setObjectName('back_to_sign_up')
        self.back_button.clicked.connect(self.switch_to_forgot_password.emit)
        ui.addWidget(self.back_button)

        ui.addStretch()

        # *----------- reset password ----------- #
        # reset_password label
        self.reset_password_label = QLabel('Reset Password')
        self.reset_password_label.setObjectName('reset_password_label')
        self.reset_password_label.setFixedHeight(100)

        # reset_password layout
        reset_password_layout = QHBoxLayout()
        reset_password_layout.addStretch()
        reset_password_layout.addWidget(self.reset_password_label)
        reset_password_layout.addStretch()
        ui.addLayout(reset_password_layout)


        # *----------- new_Password ----------- #
        # new_password label
        self.new_password_label = QLabel('New Password')
        self.new_password_label.setObjectName('new_password_label')
        self.new_password_label.setFixedSize(350,50)

        # new_password label layout
        new_password_layout = QHBoxLayout()
        new_password_layout.addStretch()
        new_password_layout.addWidget(self.new_password_label)
        new_password_layout.addStretch()
        ui.addLayout(new_password_layout)

        # new_password input box
        self.new_password_input_box = QLineEdit()
        self.new_password_input_box.setObjectName('new_password_input_box')
        self.new_password_input_box.setPlaceholderText('Type your new password')
        self.new_password_input_box.returnPressed.connect(self.new_password_enter)
        self.new_password_input_box.textChanged.connect(lambda: self.handle_text_change(self.new_password_input_box, self.new_password_input_box.text(), is_new_password=True))
        self.new_password_input_box.setFixedSize(305, 40)

        # new_password input box layout
        new_password_input_box_layout = QHBoxLayout()
        new_password_input_box_layout.setObjectName('new_password_input_box_layout')
        new_password_input_box_layout.addStretch()
        new_password_input_box_layout.addWidget(self.new_password_input_box)
        new_password_input_box_layout.addStretch()
        ui.addLayout(new_password_input_box_layout)
        self.previous_text = ''

        # todo new_password error label
        self.new_password_error_label = QLabel('')
        self.new_password_error_label.setObjectName('new_password_error_label')
        self.new_password_error_label.setFixedHeight(20)

        # todo new_password error label layout
        new_password_error_label_layout = QHBoxLayout()
        new_password_error_label_layout.setObjectName('new_password_error_label_layout')
        new_password_error_label_layout.addStretch()
        new_password_error_label_layout.addWidget(self.new_password_error_label)
        new_password_error_label_layout.addStretch()
        ui.addLayout(new_password_error_label_layout)


        # *----------- Confirm new password ----------- #
        # confirm_new_password label
        self.confirm_new_password_label = QLabel('Confirm New Password')
        self.confirm_new_password_label.setObjectName('confirm_new_password_label')
        self.confirm_new_password_label.setFixedSize(350,50)

        # confirm_new_password label layout
        confirm_new_password_label_layout = QHBoxLayout()
        confirm_new_password_label_layout.addStretch()
        confirm_new_password_label_layout.addWidget(self.confirm_new_password_label)
        confirm_new_password_label_layout.addStretch()
        ui.addLayout(confirm_new_password_label_layout)

        # confirm_new_password input box
        self.confirm_new_password_input_box = QLineEdit()
        self.confirm_new_password_input_box.setObjectName('confirm_new_password_input_box')
        self.confirm_new_password_input_box.setPlaceholderText('Type your confirm new password')
        self.confirm_new_password_input_box.returnPressed.connect(self.confirm_new_password_enter)
        self.confirm_new_password_input_box.textChanged.connect(lambda: self.handle_text_change(self.confirm_new_password_input_box, self.confirm_new_password_input_box.text(), is_new_password=False))
        self.confirm_new_password_input_box.setFixedSize(305,50)
        self.previous_confirm_new_password = ''

        # confirm_new_password input box layout
        confirm_new_password_input_box_layout = QHBoxLayout()
        confirm_new_password_input_box_layout.setObjectName('confirm_new_password_input_box_layout')
        confirm_new_password_input_box_layout.addStretch()
        confirm_new_password_input_box_layout.addWidget(self.confirm_new_password_input_box)
        confirm_new_password_input_box_layout.addStretch()
        ui.addLayout(confirm_new_password_input_box_layout)

        # todo Confirm_new_password error label
        self.confirm_new_password_error_label = QLabel('')
        self.confirm_new_password_error_label.setObjectName('confirm_new_password_error_label')
        self.confirm_new_password_error_label.setFixedHeight(20)

        # todo confirm_new_password error label layout
        confirm_new_password_error_label_layout = QHBoxLayout()
        confirm_new_password_error_label_layout.setObjectName('confirm_new_password_error_label_layout')
        confirm_new_password_error_label_layout.addStretch()
        confirm_new_password_error_label_layout.addWidget(self.confirm_new_password_error_label)
        confirm_new_password_error_label_layout.addStretch()
        ui.addLayout(confirm_new_password_error_label_layout)

        ui.addSpacing(25)

        # *---------- Reset password button ----------- #
        # sign_up button
        self.confirm = QPushButton('Confirm')
        self.confirm.setStyleSheet('background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #43d9ff, stop:1 #ff56c7);')
        self.confirm.setObjectName('confirm_button')
        self.confirm.setFixedSize(230,37)
        self.confirm.clicked.connect(self.reset_password_clicked)

        # reset_password button layout
        confirm_layout = QHBoxLayout()
        confirm_layout.setObjectName('confirm_layout')
        confirm_layout.setContentsMargins(0,10,0,65)
        confirm_layout.addStretch()
        confirm_layout.addWidget(self.confirm)
        confirm_layout.addStretch()
        ui.addLayout(confirm_layout)

        ui.addStretch()

    # * -------------------- new password to ● -------------------- * #
    def handle_text_change(self, input_box, text, is_new_password=True):
        if self.timer.isActive():
            self.timer.stop()

        self.active_input_box = input_box

        if is_new_password:
            self.real_new_password = text

            if len(text) > len(self.previous_text):
                masked_new_password = '●' * (len(text) - 1) + text[-1]
            else:
                masked_new_password = '●' * len(text)

            self.previous_text = text
            input_box.blockSignals(True)
            input_box.setText(masked_new_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_new_password))

        else:
            self.real_confirm_new_password = text

            if len(text) > len(self.previous_confirm_new_password):
                masked_confirm_new_password = '●' * (len(text) - 1) + text[-1]
            else:
                masked_confirm_new_password = '●' * len(text)

            self.previous_confirm_new_password = text
            input_box.blockSignals(True)
            input_box.setText(masked_confirm_new_password)
            input_box.blockSignals(False)
            input_box.setCursorPosition(len(masked_confirm_new_password))

        self.timer.start(700)

    # *---------- mask last character after timeout ---------- #

    def mask_last_character(self):
        self.timer.stop()
        if self.active_input_box is not None:
            if self.active_input_box == self.new_password_input_box:
                masked_new_password = '●' * len(self.real_new_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_new_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_new_password))

            elif self.active_input_box == self.confirm_new_password_input_box:
                masked_confirm_new_password = '●' * len(self.real_confirm_new_password)
                self.active_input_box.blockSignals(True)
                self.active_input_box.setText(masked_confirm_new_password)
                self.active_input_box.blockSignals(False)
                self.active_input_box.setCursorPosition(len(masked_confirm_new_password))


    # *---------- check new password enter ---------- #
    def new_password_enter(self):
        self.new_password_focus += 1
        if self.new_password_focus >= 1:
            self.check_reset_password()

        self.new_password = self.new_password_input_box.text()
        if self.new_password != '':
            self.confirm_new_password_input_box.setFocus()

    # *---------- check confirm new password enter ---------- #
    def confirm_new_password_enter(self):
        self.confirm_new_password_focus += 1
        if self.confirm_new_password_focus >= 1:
            self.check_reset_password()

    # *---------- check reset_password clicked ---------- #
    def reset_password_clicked(self):
        self.new_password = self.new_password_input_box.text()
        self.confirm_new_password = self.confirm_new_password_input_box.text()

        if self.new_password == '':
            self.new_password_enter()
        elif self.confirm_new_password == '':
            self.confirm_new_password_enter()
        else:
            self.check_reset_password()



    # *---------- check reset_password ---------- #
    def check_reset_password(self):
        valid = True


        if self.new_password == '':
            self.new_password_error_label.setText('Please enter your new password')
            self.confirm_new_password_error_label.setText('')

        elif self.confirm_new_password == '':
            self.new_password_error_label.setText('')
            if self.confirm_new_password_focus >= 1:
                self.confirm_new_password_error_label.setText('Please enter confirm new password')


        if self.new_password != '':
            self.new_password_error_label.setText('')

        if self.real_confirm_new_password != '':
            if self.real_confirm_new_password != self.real_new_password:
                self.confirm_new_password_error_label.setText('Password does not match')
            else:
                self.confirm_new_password_error_label.setText('')
                self.open_main_window()


    # # *---------- back to forgot password ----------* #
    # def back_to_forgot_password(self):
    #     from forgot_password import Forgot_password_page
    #     self.forgot_password = Forgot_password_page()
    #     self.forgot_password.show()
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
    reset_password = Reset_password()
    # Reset_password.showMaximized()
    reset_password.show()
    app.exec()
