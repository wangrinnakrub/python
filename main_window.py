from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# ? ---------- main window ---------- #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(r"C:\pic\basketball-ball.png"))
        self.setWindowTitle('Basketball Score Sheet')
        self.import_style('style_main_window.qss')


    def import_style(self, file_name):
        try:
            with open(file_name, 'r') as file:
                self.setStyleSheet(file.read())
        except FileNotFoundError:
            print(f"Error: Cannot find the file '{file_name}'")

    # def ui(self):













#! ---------- run program --------- #
if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.showMaximized()
    app.exec()
