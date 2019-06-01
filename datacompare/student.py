# -*- coding: utf-8 -*-
from util import swap
from util import filter_student_list_with_dict_key
from copy import deepcopy
import json


class StudentList:

    def __init__(self):
        self.last_semester_students = []
        self.current_semester_students = []
        self.compared_result = []
        self.filtered_compared_result = []

    def set_compared_result(self, last_semester_students, current_semester_students, filter_list):
        self.compared_result = self.get_all_unfinished_students(last_semester_students,
                                                                current_semester_students)
        self.filtered_compared_result = filter_student_list_with_dict_key(self.compared_result, filter_list)

    def set_semester_list(self, input_data_1, input_data_2):
        # Note: input_data_1 < input_data_2 may cause some problem
        if json.dumps(input_data_1) < json.dumps(input_data_2):
            input_data_1, input_data_2 = swap(input_data_1, input_data_2)

        if (input_data_1 and input_data_2) and json.dumps(input_data_1) != json.dumps(input_data_2):
            input_data_1 = self.remove_graduated_students(input_data_1)

        self.last_semester_students = input_data_1
        self.current_semester_students = input_data_2

    def get_finished_older_students(self, last_semester_students, current_semester_students):
        last_semester_students = deepcopy(last_semester_students)
        current_semester_students = deepcopy(current_semester_students)
        finished_older_students = []
        for l_student in last_semester_students:
            for index, c_student in enumerate(current_semester_students):
                if l_student['std_idno'] == c_student['std_idno']:
                    finished_older_students.append(c_student)
                    current_semester_students.pop(index)
        return finished_older_students

    def get_unfinished_older_students(self, last_semester_students, current_semester_students):
        last_semester_students = deepcopy(last_semester_students)
        current_semester_students = deepcopy(current_semester_students)
        finished_older_students = self.get_finished_older_students(last_semester_students,
                                                                            current_semester_students)
        for f_student in finished_older_students:
            for l_index, l_student in enumerate(last_semester_students):
                if f_student['std_idno'] == l_student['std_idno']:
                    last_semester_students.pop(l_index)
        unfinished_older_students = last_semester_students

        return unfinished_older_students

    def get_new_students(self, last_semester_students, current_semester_students):
        last_semester_students = deepcopy(last_semester_students)
        current_semester_students = deepcopy(current_semester_students)
        finished_older_students = self.get_finished_older_students(last_semester_students,
                                                                            current_semester_students)
        for f_student in finished_older_students:
            for c_index, c_student in enumerate(current_semester_students):
                if f_student['std_idno'] == c_student['std_idno']:
                    current_semester_students.pop(c_index)
        new_students = current_semester_students

        return new_students

    def get_all_unfinished_students(self, last_semester_students, current_semester_students):
        unfinished_older_students = self.get_unfinished_older_students(last_semester_students,
                                                                       current_semester_students)
        new_students = self.get_new_students(last_semester_students,
                                             current_semester_students)
        all_unfinished_students = unfinished_older_students + new_students

        return all_unfinished_students

    def remove_graduated_students(self, studemts):
        remained_result = []
        for dict_data in studemts:
            if dict_data['cls_name_abr'][1:3] == '五專' and dict_data['cls_name_abr'][-2] != '五':
                remained_result.append(dict_data)
            elif dict_data['cls_name_abr'][1:3] == '四技' and dict_data['cls_name_abr'][-2] != '四':
                remained_result.append(dict_data)
            elif (dict_data['cls_name_abr'][-4] == '碩' or dict_data['cls_name_abr'][-3] == '碩') and dict_data['cls_name_abr'][-2] != '二':
                remained_result.append(dict_data)
        return remained_result



