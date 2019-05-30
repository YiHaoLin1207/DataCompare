# -*- coding: utf-8 -*-
from util import get_intersection_of_two_list
from util import get_diff_of_two_list
from util import trans_json_list_to_dict_list


class StudentList:

    def __init__(self):
        self.last_semester_student_dict_list = []
        self.last_semester_student_json_list = []
        self.current_semester_student_dict_list = []
        self.current_semester_student_json_list = []

        self.final_result = []

    def get_finished_older_student(self, last_semester_student_json_list, current_semester_student_json_list):
        finished_older_student_json_list = get_intersection_of_two_list(last_semester_student_json_list,
                                                                        current_semester_student_json_list)
        return finished_older_student_json_list

    def get_unfinished_older_student(self, last_semester_student_json_list, current_semester_student_json_list):
        finished_older_student_json_list = get_intersection_of_two_list(last_semester_student_json_list,
                                                                        current_semester_student_json_list)
        unfinished_older_student_json_list = get_diff_of_two_list(last_semester_student_json_list,
                                                                  finished_older_student_json_list)
        return unfinished_older_student_json_list

    def get_new_student(self, last_semester_student_json_list, current_semester_student_json_list):
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


class FilterBase(object):
    def __init__(self):
        self.dvs_id = False
        self.dgr_id = False
        self.unt_id = False
        self.cls_id = False
        self.yms_year = False
        self.yms_sms = False
        self.cls_id = False
        self.cls_name_abr = False
        self.std_id = False
        self.std_name = False
        self.std_idno = False
        self.src_status = False
        self.kind_id = False
        self.kind_name = False
        self.std_key = False
        self.src_flag = False
        self.m1 = False
        self.m2 = False
        self.m3 = False
        self.s1 = False
        self.s2 = False
        self.s3 = False
        self.status1 = False
        self.status2 = False
        self.pass_yn = False
        self.src_kind = False
        self.s4 = False
        self.std_sex = False
        self.std_mobile = False
        self.std_tel = False


class CompareFilter:
    def __init__(self):
        super(CompareFilter, self).__init__()
        self.std_idno = True


class ResultFilter:
    def __init__(self):
        super(ResultFilter, self).__init__()
        self.std_name = True
        self.std_idno = True
        self.std_mobile = True
        self.std_tel = True



