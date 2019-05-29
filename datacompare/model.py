# -*- coding: utf-8 -*-
from util import get_intersection_of_two_list
from util import get_diff_of_two_list
from util import trans_json_list_to_dict_list
from util import input_data_is_valid


class StudentList:

    def __init__(self):
        self.last_semester_student_dict_list = []
        self.last_semester_student_json_list = []
        self.current_semester_student_dict_list = []
        self.current_semester_student_json_list = []

        self.final_result = []

    def get_finished_older_student(self, last_semester_student_json_list, current_semester_student_json_list):
        input_data_is_valid(last_semester_student_json_list, current_semester_student_json_list)
        finished_older_student_json_list = get_intersection_of_two_list(last_semester_student_json_list,
                                                                        current_semester_student_json_list)
        return finished_older_student_json_list

    def get_unfinished_older_student(self, last_semester_student_json_list, current_semester_student_json_list):
        input_data_is_valid(last_semester_student_json_list, current_semester_student_json_list)
        finished_older_student_json_list = get_intersection_of_two_list(last_semester_student_json_list,
                                                                        current_semester_student_json_list)
        unfinished_older_student_json_list = get_diff_of_two_list(last_semester_student_json_list,
                                                                  finished_older_student_json_list)
        return unfinished_older_student_json_list

    def get_new_student(self, last_semester_student_json_list, current_semester_student_json_list):
        input_data_is_valid(last_semester_student_json_list, current_semester_student_json_list)
        new_student_list = get_diff_of_two_list(current_semester_student_json_list, last_semester_student_json_list)
        return new_student_list

    def get_all_unfinished_student(self, last_semester_student_json_list, current_semester_student_json_list):

        unfinished_older_student_json_list = self.get_unfinished_older_student(last_semester_student_json_list,
                                                                               current_semester_student_json_list)
        new_student_json_list = self.get_new_student(last_semester_student_json_list,
                                                     current_semester_student_json_list)
        all_unfinished_student_json_list = unfinished_older_student_json_list + new_student_json_list
        all_unfinished_student_dict_list = trans_json_list_to_dict_list(all_unfinished_student_json_list)

        return all_unfinished_student_dict_list

    def set_final_result(self, last_semester_student_json_list, current_semester_student_json_list):

        self.final_result = self.get_all_unfinished_student(last_semester_student_json_list,
                                                            current_semester_student_json_list)
