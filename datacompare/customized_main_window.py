#coding=utf-8

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class CustomizedMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CustomizedMainWindow, self).__init__()

    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu = QtWidgets.QMenu(self)
        return self.contextMenu

    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.move(self.pos() + pos)
        self.contextMenu.show()
