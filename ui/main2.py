import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMainWindow, QAction, qApp, QMenu, QPushButton
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
from PyQt5 import QtGui


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.logo_icon = '..\\images\\schoolLogo.PNG'
        self.start_icon = '..\\images\\play-button.png'
        self.wide = 800
        self.length = 600
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Statusbar')
        self.resize(self.wide, self.length)
        self.setWindowIcon(QIcon(self.logo_icon))
        self.statusBar().showMessage('Ready')

        self.set_start_button()
        self.set_btn_font_size(self.start_comparing_btn, 20)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_start_button(self):
        self.start_comparing_btn = QPushButton(self)
        self.start_comparing_btn.setText("開始比對")
        self.start_comparing_btn.setIcon(QIcon(self.start_icon))
        self.start_comparing_btn.setIconSize(QSize(20, 20))
        self.start_comparing_btn.resize(150, 50)
        self.start_comparing_btn.move(600, 500)

    def set_btn_font_size(self, btn, size):
        font = QFont('Courier')  # lineedit current font
        font.setPointSize(size)  # change it's size
        btn.setFont(font)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
