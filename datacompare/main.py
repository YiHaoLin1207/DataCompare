# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from model import StudentList
from model import CompareFilter
from model import ResultFilter
from util import load_txt_file_as_dict_list
from util import filter_student_list_with_dict_key
from util import swap


class Ui_MainWindow(object):
    def __init__(self):
        self.student_list = StudentList()
        self.compare_filter = CompareFilter()
        self.result_filter = ResultFilter()
        self.input_data_1 = []
        self.input_data_2 = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 608)
        MainWindow.setDocumentMode(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(570, 510, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.startBtn.setFont(font)
        self.startBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(lambda: self.set_semester_list(self.input_data_1, self.input_data_2))
        self.startBtn.clicked.connect(lambda: self.student_list.set_compared_result(
            self.student_list.last_semester_student_dict_list,
            self.student_list.current_semester_student_dict_list))
        self.startBtn.clicked.connect(lambda: self.show_result(self.student_list.final_result))

        self.MatchedResultTable = QtWidgets.QTableWidget(self.centralwidget)
        self.MatchedResultTable.setGeometry(QtCore.QRect(30, 20, 471, 461))
        self.MatchedResultTable.setObjectName("MatchedResultTable")
        self.MatchedResultTable.setColumnCount(0)
        self.MatchedResultTable.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(230, 260, 120, 80))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 490, 471, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 40, 471, 31))
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
        self.FileTwoBrowseBtn.clicked.connect(self.set_input_data_2)
        self.horizontalLayout_3.addWidget(self.FileTwoBrowseBtn)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 471, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.FileOneLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.FileOneLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FileOneLabel.setObjectName("FileOneLabel")
        self.horizontalLayout_2.addWidget(self.FileOneLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.FileOneBrowseBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.FileOneBrowseBtn.setObjectName("FileOneBrowseBtn")
        self.FileOneBrowseBtn.clicked.connect(self.set_input_data_1)
        self.horizontalLayout_2.addWidget(self.FileOneBrowseBtn)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(510, 20, 281, 461))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 240, 261, 221))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.result_condition = QtWidgets.QLabel(self.layoutWidget_2)
        self.result_condition.setObjectName("result_condition")
        self.gridLayout_2.addWidget(self.result_condition, 0, 0, 1, 1)
        self.result_cls_id = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_cls_id.setObjectName("result_cls_id")
        self.gridLayout_2.addWidget(self.result_cls_id, 1, 0, 1, 1)
        self.result_s1 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_s1.setObjectName("result_s1")
        self.gridLayout_2.addWidget(self.result_s1, 1, 1, 1, 1)
        self.result_std_idno = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_idno.setObjectName("result_std_idno")
        self.result_std_idno.setCheckState(self.result_filter.std_idno)
        self.result_std_idno.stateChanged.connect(self.set_result_std_idno)
        self.gridLayout_2.addWidget(self.result_std_idno, 1, 2, 1, 1)
        self.result_cls_name_abr = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_cls_name_abr.setObjectName("result_cls_name_abr")
        self.gridLayout_2.addWidget(self.result_cls_name_abr, 2, 0, 1, 1)
        self.result_s2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_s2.setObjectName("result_s2")
        self.gridLayout_2.addWidget(self.result_s2, 2, 1, 1, 1)
        self.result_std_key = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_key.setObjectName("result_std_key")
        self.gridLayout_2.addWidget(self.result_std_key, 2, 2, 1, 1)
        self.result_dgr_id = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_dgr_id.setObjectName("result_dgr_id")
        self.gridLayout_2.addWidget(self.result_dgr_id, 3, 0, 1, 1)
        self.result_s3 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_s3.setObjectName("result_s3")
        self.gridLayout_2.addWidget(self.result_s3, 3, 1, 1, 1)
        self.result_std_mobile = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_mobile.setObjectName("result_std_mobile")
        self.gridLayout_2.addWidget(self.result_std_mobile, 3, 2, 1, 1)
        self.result_dvs_id = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_dvs_id.setObjectName("result_dvs_id")
        self.gridLayout_2.addWidget(self.result_dvs_id, 4, 0, 1, 1)
        self.result_s4 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_s4.setObjectName("result_s4")
        self.gridLayout_2.addWidget(self.result_s4, 4, 1, 1, 1)
        self.result_std_name = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_name.setObjectName("result_std_name")
        self.gridLayout_2.addWidget(self.result_std_name, 4, 2, 1, 1)
        self.result_kind_id = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_kind_id.setObjectName("result_kind_id")
        self.gridLayout_2.addWidget(self.result_kind_id, 5, 0, 1, 1)
        self.result_status1 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_status1.setObjectName("result_status1")
        self.gridLayout_2.addWidget(self.result_status1, 5, 1, 1, 1)
        self.result_std_sex = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_sex.setObjectName("result_std_sex")
        self.gridLayout_2.addWidget(self.result_std_sex, 5, 2, 1, 1)
        self.result_kind_name = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_kind_name.setObjectName("result_kind_name")
        self.gridLayout_2.addWidget(self.result_kind_name, 6, 0, 1, 1)
        self.result_status2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_status2.setObjectName("result_status2")
        self.gridLayout_2.addWidget(self.result_status2, 6, 1, 1, 1)
        self.result_std_tel = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_tel.setObjectName("result_std_tel")
        self.gridLayout_2.addWidget(self.result_std_tel, 6, 2, 1, 1)
        self.result_m1 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_m1.setObjectName("result_m1")
        self.gridLayout_2.addWidget(self.result_m1, 7, 0, 1, 1)
        self.result_src_flag = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_src_flag.setObjectName("result_src_flag")
        self.gridLayout_2.addWidget(self.result_src_flag, 7, 1, 1, 1)
        self.result_unt_id = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_unt_id.setObjectName("result_unt_id")
        self.gridLayout_2.addWidget(self.result_unt_id, 7, 2, 1, 1)
        self.result_m2 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_m2.setObjectName("result_m2")
        self.gridLayout_2.addWidget(self.result_m2, 8, 0, 1, 1)
        self.result_src_kind = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_src_kind.setObjectName("result_src_kind")
        self.gridLayout_2.addWidget(self.result_src_kind, 8, 1, 1, 1)
        self.result_yms_sms = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_yms_sms.setObjectName("result_yms_sms")
        self.gridLayout_2.addWidget(self.result_yms_sms, 8, 2, 1, 1)
        self.result_m3 = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_m3.setObjectName("result_m3")
        self.gridLayout_2.addWidget(self.result_m3, 9, 0, 1, 1)
        self.result_src_status = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_src_status.setObjectName("result_src_status")
        self.gridLayout_2.addWidget(self.result_src_status, 9, 1, 1, 1)
        self.result_pass_yn = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_pass_yn.setObjectName("result_pass_yn")
        self.gridLayout_2.addWidget(self.result_pass_yn, 10, 0, 1, 1)
        self.result_std_id = QtWidgets.QCheckBox(self.layoutWidget_2)
        self.result_std_id.setObjectName("result_std_id")
        self.gridLayout_2.addWidget(self.result_std_id, 10, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.frame_2)
        self.widget1.setGeometry(QtCore.QRect(10, 0, 261, 221))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.select_condition = QtWidgets.QLabel(self.widget1)
        self.select_condition.setObjectName("select_condition")
        self.gridLayout.addWidget(self.select_condition, 0, 0, 1, 1)
        self.compare_cls_id = QtWidgets.QCheckBox(self.widget1)
        self.compare_cls_id.setObjectName("compare_cls_id")
        self.gridLayout.addWidget(self.compare_cls_id, 1, 0, 1, 1)
        self.compare_s1 = QtWidgets.QCheckBox(self.widget1)
        self.compare_s1.setObjectName("compare_s1")
        self.gridLayout.addWidget(self.compare_s1, 1, 1, 1, 1)
        self.compare_std_idno = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_idno.setObjectName("compare_std_idno")
        self.gridLayout.addWidget(self.compare_std_idno, 1, 2, 1, 1)
        self.compare_cls_name_abr = QtWidgets.QCheckBox(self.widget1)
        self.compare_cls_name_abr.setObjectName("compare_cls_name_abr")
        self.gridLayout.addWidget(self.compare_cls_name_abr, 2, 0, 1, 1)
        self.compare_s2 = QtWidgets.QCheckBox(self.widget1)
        self.compare_s2.setObjectName("compare_s2")
        self.gridLayout.addWidget(self.compare_s2, 2, 1, 1, 1)
        self.compare_std_key = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_key.setObjectName("compare_std_key")
        self.gridLayout.addWidget(self.compare_std_key, 2, 2, 1, 1)
        self.compare_dgr_id = QtWidgets.QCheckBox(self.widget1)
        self.compare_dgr_id.setObjectName("compare_dgr_id")
        self.gridLayout.addWidget(self.compare_dgr_id, 3, 0, 1, 1)
        self.compare_s3 = QtWidgets.QCheckBox(self.widget1)
        self.compare_s3.setObjectName("compare_s3")
        self.gridLayout.addWidget(self.compare_s3, 3, 1, 1, 1)
        self.compare_std_mobile = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_mobile.setObjectName("compare_std_mobile")
        self.gridLayout.addWidget(self.compare_std_mobile, 3, 2, 1, 1)
        self.compare_dvs_id = QtWidgets.QCheckBox(self.widget1)
        self.compare_dvs_id.setObjectName("compare_dvs_id")
        self.gridLayout.addWidget(self.compare_dvs_id, 4, 0, 1, 1)
        self.compare_s4 = QtWidgets.QCheckBox(self.widget1)
        self.compare_s4.setObjectName("compare_s4")
        self.gridLayout.addWidget(self.compare_s4, 4, 1, 1, 1)
        self.compare_std_name = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_name.setObjectName("compare_std_name")
        self.gridLayout.addWidget(self.compare_std_name, 4, 2, 1, 1)
        self.compare_kind_id = QtWidgets.QCheckBox(self.widget1)
        self.compare_kind_id.setObjectName("compare_kind_id")
        self.gridLayout.addWidget(self.compare_kind_id, 5, 0, 1, 1)
        self.compare_status1 = QtWidgets.QCheckBox(self.widget1)
        self.compare_status1.setObjectName("compare_status1")
        self.gridLayout.addWidget(self.compare_status1, 5, 1, 1, 1)
        self.compare_std_sex = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_sex.setObjectName("compare_std_sex")
        self.gridLayout.addWidget(self.compare_std_sex, 5, 2, 1, 1)
        self.compare_kind_name = QtWidgets.QCheckBox(self.widget1)
        self.compare_kind_name.setObjectName("compare_kind_name")
        self.gridLayout.addWidget(self.compare_kind_name, 6, 0, 1, 1)
        self.compare_status2 = QtWidgets.QCheckBox(self.widget1)
        self.compare_status2.setObjectName("compare_status2")
        self.gridLayout.addWidget(self.compare_status2, 6, 1, 1, 1)
        self.compare_std_tel = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_tel.setObjectName("compare_std_tel")
        self.gridLayout.addWidget(self.compare_std_tel, 6, 2, 1, 1)
        self.compare_m1 = QtWidgets.QCheckBox(self.widget1)
        self.compare_m1.setObjectName("compare_m1")
        self.gridLayout.addWidget(self.compare_m1, 7, 0, 1, 1)
        self.compare_src_flag = QtWidgets.QCheckBox(self.widget1)
        self.compare_src_flag.setObjectName("compare_src_flag")
        self.gridLayout.addWidget(self.compare_src_flag, 7, 1, 1, 1)
        self.compare_unt_id = QtWidgets.QCheckBox(self.widget1)
        self.compare_unt_id.setObjectName("compare_unt_id")
        self.gridLayout.addWidget(self.compare_unt_id, 7, 2, 1, 1)
        self.compare_m2 = QtWidgets.QCheckBox(self.widget1)
        self.compare_m2.setObjectName("compare_m2")
        self.gridLayout.addWidget(self.compare_m2, 8, 0, 1, 1)
        self.compare_src_kind = QtWidgets.QCheckBox(self.widget1)
        self.compare_src_kind.setObjectName("compare_src_kind")
        self.gridLayout.addWidget(self.compare_src_kind, 8, 1, 1, 1)
        self.compare_yms_sms = QtWidgets.QCheckBox(self.widget1)
        self.compare_yms_sms.setObjectName("compare_yms_sms")
        self.gridLayout.addWidget(self.compare_yms_sms, 8, 2, 1, 1)
        self.compare_m3 = QtWidgets.QCheckBox(self.widget1)
        self.compare_m3.setObjectName("compare_m3")
        self.gridLayout.addWidget(self.compare_m3, 9, 0, 1, 1)
        self.compare_src_status = QtWidgets.QCheckBox(self.widget1)
        self.compare_src_status.setObjectName("compare_src_status")
        self.gridLayout.addWidget(self.compare_src_status, 9, 1, 1, 1)
        self.compare_pass_yn = QtWidgets.QCheckBox(self.widget1)
        self.compare_pass_yn.setObjectName("compare_pass_yn")
        self.gridLayout.addWidget(self.compare_pass_yn, 10, 0, 1, 1)
        self.compare_std_id = QtWidgets.QCheckBox(self.widget1)
        self.compare_std_id.setObjectName("compare_std_id")
        self.gridLayout.addWidget(self.compare_std_id, 10, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "開始比對"))
        self.FileTwoLable.setText(_translate("MainWindow", "檔案 2"))
        self.FileTwoBrowseBtn.setText(_translate("MainWindow", "瀏覽..."))
        self.FileOneLabel.setText(_translate("MainWindow", "檔案 1"))
        self.FileOneBrowseBtn.setText(_translate("MainWindow", "瀏覽..."))
        self.result_condition.setText(_translate("MainWindow", "結果條件篩選"))
        self.result_cls_id.setText(_translate("MainWindow", "cls_id"))
        self.result_s1.setText(_translate("MainWindow", "s1"))
        self.result_std_idno.setText(_translate("MainWindow", "std_idno"))
        self.result_cls_name_abr.setText(_translate("MainWindow", "cls_name_abr"))
        self.result_s2.setText(_translate("MainWindow", "s2"))
        self.result_std_key.setText(_translate("MainWindow", "std_key"))
        self.result_dgr_id.setText(_translate("MainWindow", "dgr_id"))
        self.result_s3.setText(_translate("MainWindow", "s3"))
        self.result_std_mobile.setText(_translate("MainWindow", "std_mobile"))
        self.result_dvs_id.setText(_translate("MainWindow", "dvs_id"))
        self.result_s4.setText(_translate("MainWindow", "s4"))
        self.result_std_name.setText(_translate("MainWindow", "std_name"))
        self.result_kind_id.setText(_translate("MainWindow", "kind_id"))
        self.result_status1.setText(_translate("MainWindow", "status1"))
        self.result_std_sex.setText(_translate("MainWindow", "std_sex"))
        self.result_kind_name.setText(_translate("MainWindow", "kind_name"))
        self.result_status2.setText(_translate("MainWindow", "status2"))
        self.result_std_tel.setText(_translate("MainWindow", "std_tel"))
        self.result_m1.setText(_translate("MainWindow", "m1"))
        self.result_src_flag.setText(_translate("MainWindow", "src_flag"))
        self.result_unt_id.setText(_translate("MainWindow", "unt_id"))
        self.result_m2.setText(_translate("MainWindow", "m2"))
        self.result_src_kind.setText(_translate("MainWindow", "src_kind"))
        self.result_yms_sms.setText(_translate("MainWindow", "yms_sms"))
        self.result_m3.setText(_translate("MainWindow", "m3"))
        self.result_src_status.setText(_translate("MainWindow", "src_status"))
        self.result_pass_yn.setText(_translate("MainWindow", "pass_yn"))
        self.result_std_id.setText(_translate("MainWindow", "std_id"))
        self.select_condition.setText(_translate("MainWindow", "比對條件篩選"))
        self.compare_cls_id.setText(_translate("MainWindow", "cls_id"))
        self.compare_s1.setText(_translate("MainWindow", "s1"))
        self.compare_std_idno.setText(_translate("MainWindow", "std_idno"))
        self.compare_cls_name_abr.setText(_translate("MainWindow", "cls_name_abr"))
        self.compare_s2.setText(_translate("MainWindow", "s2"))
        self.compare_std_key.setText(_translate("MainWindow", "std_key"))
        self.compare_dgr_id.setText(_translate("MainWindow", "dgr_id"))
        self.compare_s3.setText(_translate("MainWindow", "s3"))
        self.compare_std_mobile.setText(_translate("MainWindow", "std_mobile"))
        self.compare_dvs_id.setText(_translate("MainWindow", "dvs_id"))
        self.compare_s4.setText(_translate("MainWindow", "s4"))
        self.compare_std_name.setText(_translate("MainWindow", "std_name"))
        self.compare_kind_id.setText(_translate("MainWindow", "kind_id"))
        self.compare_status1.setText(_translate("MainWindow", "status1"))
        self.compare_std_sex.setText(_translate("MainWindow", "std_sex"))
        self.compare_kind_name.setText(_translate("MainWindow", "kind_name"))
        self.compare_status2.setText(_translate("MainWindow", "status2"))
        self.compare_std_tel.setText(_translate("MainWindow", "std_tel"))
        self.compare_m1.setText(_translate("MainWindow", "m1"))
        self.compare_src_flag.setText(_translate("MainWindow", "src_flag"))
        self.compare_unt_id.setText(_translate("MainWindow", "unt_id"))
        self.compare_m2.setText(_translate("MainWindow", "m2"))
        self.compare_src_kind.setText(_translate("MainWindow", "src_kind"))
        self.compare_yms_sms.setText(_translate("MainWindow", "yms_sms"))
        self.compare_m3.setText(_translate("MainWindow", "m3"))
        self.compare_src_status.setText(_translate("MainWindow", "src_status"))
        self.compare_pass_yn.setText(_translate("MainWindow", "pass_yn"))
        self.compare_std_id.setText(_translate("MainWindow", "std_id"))

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

    def set_input_data_1(self):
        file_name = self.get_file_name_from_browse_slot(self.lineEdit)
        dict_list_data = load_txt_file_as_dict_list(file_name)
        self.input_data_1 = dict_list_data

    def set_input_data_2(self):
        file_name = self.get_file_name_from_browse_slot(self.lineEdit_2)
        dict_list_data = load_txt_file_as_dict_list(file_name)
        self.input_data_2 = dict_list_data

    def set_semester_list(self, input_data_1, input_data_2):
        # Note: input_data_1 < input_data_2 may cause some problem
        if input_data_1 < input_data_2:
            input_data_1, input_data_2 = swap(input_data_1, input_data_2)

        filtered_data_list_1 = filter_student_list_with_dict_key(input_data_1)
        filtered_data_list_2 = filter_student_list_with_dict_key(input_data_2)
        self.student_list.last_semester_student_dict_list = filtered_data_list_1
        self.student_list.current_semester_student_dict_list = filtered_data_list_2
        print(self.student_list)

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

    def set_result_std_idno(self, state):

        if state == QtCore.Qt.Checked:
            self.result_filter.std_idno = QtCore.Qt.Checked
        else:
            self.result_filter.std_idno = QtCore.Qt.Unchecked

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