# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from util import get_intersection_of_two_list
from util import get_diff_of_two_list


class StudentList:

    def __init__(self):
        self.last_semester_student_dict_list = []
        self.current_semester_student_dict_list = []
        self.final_result = []

    def get_finished_older_student(self, last_semester_student_dict_list, current_semester_student_dict_list):
        finished_older_student_dict_list = get_intersection_of_two_list(last_semester_student_dict_list,
                                                                        current_semester_student_dict_list)
        return finished_older_student_dict_list

    def get_unfinished_older_student(self, last_semester_student_dict_list, current_semester_student_dict_list):
        finished_older_student_dict_list = get_intersection_of_two_list(last_semester_student_dict_list,
                                                                        current_semester_student_dict_list)
        unfinished_older_student_dict_list = get_diff_of_two_list(last_semester_student_dict_list,
                                                                  finished_older_student_dict_list)
        return unfinished_older_student_dict_list

    def get_new_student(self, last_semester_student_dict_list, current_semester_student_dict_list):
        new_student_list = get_diff_of_two_list(current_semester_student_dict_list, last_semester_student_dict_list)
        return new_student_list

    def get_all_unfinished_student(self, last_semester_student_dict_list, current_semester_student_dict_list):
        unfinished_older_student_dict_list = self.get_unfinished_older_student(last_semester_student_dict_list,
                                                                               current_semester_student_dict_list)
        new_student_dict_list = self.get_new_student(last_semester_student_dict_list,
                                                     current_semester_student_dict_list)
        all_unfinished_student_dict_list = unfinished_older_student_dict_list + new_student_dict_list

        return all_unfinished_student_dict_list

    def set_compared_result(self, last_semester_student_dict_list, current_semester_student_dict_list):
        self.final_result = self.get_all_unfinished_student(last_semester_student_dict_list,
                                                            current_semester_student_dict_list)


class BaseFilter(object):
    def __init__(self):
        self.dvs_id = QtCore.Qt.Unchecked
        self.dgr_id = QtCore.Qt.Unchecked
        self.unt_id = QtCore.Qt.Unchecked
        self.cls_id = QtCore.Qt.Unchecked
        self.yms_year = QtCore.Qt.Unchecked
        self.yms_sms = QtCore.Qt.Unchecked
        self.cls_id = QtCore.Qt.Unchecked
        self.cls_name_abr = QtCore.Qt.Unchecked
        self.std_id = QtCore.Qt.Unchecked
        self.std_name = QtCore.Qt.Unchecked
        self.std_idno = QtCore.Qt.Unchecked
        self.src_status = QtCore.Qt.Unchecked
        self.kind_id = QtCore.Qt.Unchecked
        self.kind_name = QtCore.Qt.Unchecked
        self.std_key = QtCore.Qt.Unchecked
        self.src_flag = QtCore.Qt.Unchecked
        self.m1 = QtCore.Qt.Unchecked
        self.m2 = QtCore.Qt.Unchecked
        self.m3 = QtCore.Qt.Unchecked
        self.s1 = QtCore.Qt.Unchecked
        self.s2 = QtCore.Qt.Unchecked
        self.s3 = QtCore.Qt.Unchecked
        self.status1 = QtCore.Qt.Unchecked
        self.status2 = QtCore.Qt.Unchecked
        self.pass_yn = QtCore.Qt.Unchecked
        self.src_kind = QtCore.Qt.Unchecked
        self.s4 = QtCore.Qt.Unchecked
        self.std_sex = QtCore.Qt.Unchecked
        self.std_mobile = QtCore.Qt.Unchecked
        self.std_tel = QtCore.Qt.Unchecked


class CompareFilter(BaseFilter):
    def __init__(self):
        super(CompareFilter, self).__init__()
        self.std_idno = QtCore.Qt.Checked


class ResultFilter(BaseFilter):
    def __init__(self):
        super(ResultFilter, self).__init__()
        self.std_name = QtCore.Qt.Checked
        self.std_idno = QtCore.Qt.Checked
        self.std_mobile = QtCore.Qt.Checked
        self.std_tel = QtCore.Qt.Checked



