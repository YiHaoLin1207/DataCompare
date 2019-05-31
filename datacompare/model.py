# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from util import swap
from util import filter_student_list_with_dict_key
from copy import deepcopy
import json


class StudentList:

    def __init__(self):
        self.last_semester_student_dict_list = []
        self.current_semester_student_dict_list = []
        self.compared_result = []
        self.filtered_compared_result = []

    def set_compared_result(self, last_semester_student_dict_list, current_semester_student_dict_list, filter_list):
        self.compared_result = self.get_all_unfinished_student(last_semester_student_dict_list,
                                                               current_semester_student_dict_list)
        self.filtered_compared_result = filter_student_list_with_dict_key(self.compared_result, filter_list)

    def set_semester_list(self, input_data_1, input_data_2):
        # Note: input_data_1 < input_data_2 may cause some problem
        if json.dumps(input_data_1) < json.dumps(input_data_2):
            input_data_1, input_data_2 = swap(input_data_1, input_data_2)

        if input_data_1 and input_data_2:
            input_data_1 = self.remove_graduated_student(input_data_1)

        self.last_semester_student_dict_list = input_data_1
        self.current_semester_student_dict_list = input_data_2

    def get_finished_older_students(self, last_semester_student_dict_list, current_semester_student_dict_list):
        last_semester_student_dict_list = deepcopy(last_semester_student_dict_list)
        current_semester_student_dict_list = deepcopy(current_semester_student_dict_list)
        finished_older_student_dict_list = []
        for l_student in last_semester_student_dict_list:
            for index, c_student in enumerate(current_semester_student_dict_list):
                if l_student['std_idno'] == c_student['std_idno']:
                    finished_older_student_dict_list.append(c_student)
                    current_semester_student_dict_list.pop(index)
        return finished_older_student_dict_list

    def get_unfinished_older_students(self, last_semester_student_dict_list, current_semester_student_dict_list):
        last_semester_student_dict_list = deepcopy(last_semester_student_dict_list)
        current_semester_student_dict_list = deepcopy(current_semester_student_dict_list)
        finished_older_student_dict_list = self.get_finished_older_students(last_semester_student_dict_list,
                                                                            current_semester_student_dict_list)
        for f_student in finished_older_student_dict_list:
            for l_index, l_student in enumerate(last_semester_student_dict_list):
                if f_student['std_idno'] == l_student['std_idno']:
                    last_semester_student_dict_list.pop(l_index)
        unfinished_older_student_dict_list = last_semester_student_dict_list

        return unfinished_older_student_dict_list

    def get_new_students(self, last_semester_student_dict_list, current_semester_student_dict_list):
        last_semester_student_dict_list = deepcopy(last_semester_student_dict_list)
        current_semester_student_dict_list = deepcopy(current_semester_student_dict_list)
        finished_older_student_dict_list = self.get_finished_older_students(last_semester_student_dict_list,
                                                                            current_semester_student_dict_list)
        for f_student in finished_older_student_dict_list:
            for c_index, c_student in enumerate(current_semester_student_dict_list):
                if f_student['std_idno'] == c_student['std_idno']:
                    current_semester_student_dict_list.pop(c_index)
        new_student_dict_list = current_semester_student_dict_list

        return new_student_dict_list

    def get_all_unfinished_student(self, last_semester_student_dict_list, current_semester_student_dict_list):
        unfinished_older_student_dict_list = self.get_unfinished_older_students(last_semester_student_dict_list,
                                                                                current_semester_student_dict_list)
        new_student_dict_list = self.get_new_students(last_semester_student_dict_list,
                                                      current_semester_student_dict_list)
        all_unfinished_student_dict_list = unfinished_older_student_dict_list + new_student_dict_list

        return all_unfinished_student_dict_list

    def remove_graduated_student(self, studemt_dict_list):
        remained_result = []
        for dict_data in studemt_dict_list:
            if dict_data['cls_name_abr'][1:3] == '五專' and dict_data['cls_name_abr'][-2] != '五':
                remained_result.append(dict_data)
            elif dict_data['cls_name_abr'][1:3] == '四技' and dict_data['cls_name_abr'][-2] != '四':
                remained_result.append(dict_data)
            elif (dict_data['cls_name_abr'][-4] == '碩' or dict_data['cls_name_abr'][-3] == '碩') and dict_data['cls_name_abr'][-2] != '二':
                remained_result.append(dict_data)
        return remained_result


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



