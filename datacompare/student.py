# -*- coding: utf-8 -*-
from util import filter_student_list_with_dict_key
from copy import deepcopy



class StudentList:

    def __init__(self):
        self.last_semester_students = []
        self.current_semester_students = []
        self.filtered_unhanded_student_result = []
        self.filtered_handed_student_result = []

    def set_unhanded_student_result(self, last_semester_students, current_semester_students, filter_list):
        unhanded_student_result = self.get_unfinished_students(last_semester_students,
                                                               current_semester_students)
        self.filtered_unhanded_student_result = filter_student_list_with_dict_key(unhanded_student_result,
                                                                                  filter_list)

    def set_handed_student_result(self, last_semester_students, current_semester_students, filter_list):
        handed_older_student_result = self.get_finished_older_students(last_semester_students,
                                                                       current_semester_students)
        handed_new_student_result = self.get_finished_new_students(last_semester_students,
                                                                   current_semester_students)
        handed_student_result = handed_older_student_result + handed_new_student_result
        self.filtered_handed_student_result = filter_student_list_with_dict_key(handed_student_result,
                                                                                filter_list)

    def set_semester_list(self, input_data_1, input_data_2):
        if input_data_1 and input_data_2:
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

    def get_unfinished_students(self, last_semester_students, current_semester_students):
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

    def get_finished_new_students(self, last_semester_students, current_semester_students):
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



