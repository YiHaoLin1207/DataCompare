#coding=utf-8

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class CustomizedQTableWidget(QtWidgets.QTableWidget):
    def __init__(self, *args, **kwargs):
        super(CustomizedQTableWidget, self).__init__(*args, **kwargs)
        self.createContextMenu()

    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)
        self.contextMenu = QtWidgets.QMenu(self)

        self.copy = QtWidgets.QAction('複製')
        self.contextMenu.addAction(self.copy)
        self.copy.triggered.connect(self.copySelectedContent)

    def showContextMenu(self, pos):
        # 菜单显示前，将它移动到鼠标点击的位置
        self.contextMenu.move(self.mapToGlobal(pos))
        self.contextMenu.show()

    def copySelectedContent(self):
        columns_num = 0
        for index in self.selectionModel().selectedIndexes():
            if index.column() == 0 and index.row() == 0:
                columns_num += 1
            elif index.column() != 0 and index.row() == 0:
                columns_num += 1

        clipboard = ""
        for count, item in enumerate(self.selectedItems()):
            if (count + 1) % columns_num == 0:
                clipboard += item.text() + '\n'
            else:
                clipboard += item.text() + '\t'

        sys_clip = QtWidgets.QApplication.clipboard()
        sys_clip.setText(clipboard)
