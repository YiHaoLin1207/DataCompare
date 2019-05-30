# -*- coding: utf-8 -*-


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from model import StudentList
from util import load_txt_file_to_json_list
from util import trans_json_list_to_dict_list
from util import filter_student_list_with_dict_key
from util import swap


class Ui_MainWindow(object):
    def __init__(self):
        self.student_list = StudentList()
        self.input_data_list_1 = []
        self.input_data_list_2 = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 608)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(610, 490, 161, 41))
        self.startBtn.clicked.connect(lambda: self.set_semester_list(self.input_data_list_1, self.input_data_list_2))
        self.startBtn.clicked.connect(lambda: self.student_list.set_final_result(
                                                                self.student_list.last_semester_student_json_list,
                                                                self.student_list.current_semester_student_json_list))
        self.startBtn.clicked.connect(lambda: self.show_result(self.student_list.final_result))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.startBtn.setFont(font)
        self.startBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startBtn.setObjectName("startBtn")
        self.MatchedResultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.MatchedResultTable.setGeometry(QtCore.QRect(30, 20, 741, 441))
        self.MatchedResultTable.setObjectName("MatchedResultTable")
        self.MatchedResultTable.setColumnCount(0)
        self.MatchedResultTable.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 260, 120, 80))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 480, 561, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 551, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.FileTwoLable = QtWidgets.QLabel(self.layoutWidget)
        self.FileTwoLable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FileTwoLable.setObjectName("FileTwoLable")
        self.horizontalLayout_3.addWidget(self.FileTwoLable)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.FileTwoBrowseBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.FileTwoBrowseBtn.setObjectName("FileTwoBrowseBtn")
        self.FileTwoBrowseBtn.clicked.connect(self.set_input_data_list_2)
        self.horizontalLayout_3.addWidget(self.FileTwoBrowseBtn)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(0, 10, 551, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.FileOneLabel = QtWidgets.QLabel(self.widget1)
        self.FileOneLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FileOneLabel.setObjectName("FileOneLabel")
        self.horizontalLayout_2.addWidget(self.FileOneLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.FileOneBrowseBtn = QtWidgets.QPushButton(self.widget1)
        self.FileOneBrowseBtn.setObjectName("FileOneBrowseBtn")
        self.FileOneBrowseBtn.clicked.connect(self.set_input_data_list_1)
        self.horizontalLayout_2.addWidget(self.FileOneBrowseBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "開始比對"))
        self.FileTwoLable.setText(_translate("MainWindow", "檔案 2"))
        self.FileTwoBrowseBtn.setText(_translate("MainWindow", "瀏覽..."))
        self.FileOneLabel.setText(_translate("MainWindow", "檔案 1"))
        self.FileOneBrowseBtn.setText(_translate("MainWindow", "瀏覽..."))

    def get_file_name_from_browse_slot(self, line_edit):
        # self.debugPrint( "Browse button pressed" )
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Text (*.txt)",
            options=options)
        self.refresh_line_edit(line_edit, file_name)
        return file_name

    def set_input_data_list_1(self):
        file_name = self.get_file_name_from_browse_slot(self.lineEdit)
        json_list_data = load_txt_file_to_json_list(file_name)
        self.input_data_list_1 = json_list_data
        print(self.input_data_list_1)

    def set_input_data_list_2(self):
        file_name = self.get_file_name_from_browse_slot(self.lineEdit_2)
        json_list_data = load_txt_file_to_json_list(file_name)
        self.input_data_list_2 = json_list_data

    def set_semester_list(self, input_data_list_1, input_data_list_2):
        if input_data_list_1 < input_data_list_2:
            input_data_list_1, input_data_list_2 = swap(input_data_list_1, input_data_list_2)
        filtered_data_list_1 = filter_student_list_with_dict_key(input_data_list_1)
        filtered_data_list_2 = filter_student_list_with_dict_key(input_data_list_2)
        self.student_list.last_semester_student_json_list = filtered_data_list_1
        dict_list_data = trans_json_list_to_dict_list(filtered_data_list_1)
        self.student_list.last_semester_student_dict_list = dict_list_data
        self.student_list.current_semester_student_json_list = filtered_data_list_2
        dict_list_data_2 = trans_json_list_to_dict_list(input_data_list_2)
        self.student_list.current_semester_student_dict_list = dict_list_data_2

    def get_row_and_column_number(self, data):
        if not data:
            return 1, 1
        row_count = len(data) + 1  # one more for title
        column_count = len(data[0])
        return row_count, column_count

    def set_widget_table_row_and_column(self, data):
        row_count, column_count = self.get_row_and_column_number(data)
        self.MatchedResultTable.setRowCount(row_count)
        self.MatchedResultTable.setColumnCount(column_count)

    def show_result(self, data):
        self.set_widget_table_row_and_column(data)
        if data:
            title_list = list(data[0].keys())
            for row_no in range(self.MatchedResultTable.rowCount()):
                for column_no in range(self.MatchedResultTable.columnCount()):
                    if row_no == 0:
                        column_title = title_list[column_no]
                        self.MatchedResultTable.setItem(row_no,
                                                        column_no,
                                                        QtWidgets.QTableWidgetItem(column_title))
                    else:
                        data_value = str(list(data[row_no - 1].values())[column_no])
                        self.MatchedResultTable.setItem(row_no,
                                                        column_no,
                                                        QtWidgets.QTableWidgetItem(data_value))
        else:
            self.MatchedResultTable.setItem(0, 0, QtWidgets.QTableWidgetItem("兩筆資料完全相符"))

    def refresh_line_edit(self, line_edit, file_name):
        line_edit.setText(file_name)


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
