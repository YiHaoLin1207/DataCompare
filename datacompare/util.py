# -*- coding: utf-8 -*-
import json


def swap(list_a, list_b):
    temp_list = list_b
    list_b = list_a
    list_a = temp_list
    return list_a, list_b


def trans_json_list_to_dict_list(json_list_data):
    if not json_list_data:
        return []
    dict_list_data = []
    for json_data in json_list_data:
        try:
            dict_list_data.append(json.loads(json_data))
        except json.decoder.JSONDecodeError:
            raise ValueError('json_list_data should contain loadable json string')
    return dict_list_data


def get_intersection_of_two_list(list_a, list_b):
    if not list_a or not list_b:
        return []
    if list_a < list_b:
        list_a, list_b = swap(list_a, list_b)
    intersection = list(set(list_a) & set(list_b))
    intersection = [x for x in list_b if x in intersection]
    return intersection


def get_diff_of_two_list(list_a, list_b):
    diff = list(set(list_a) - set(list_b))
    diff = [x for x in list_a if x in diff]
    return diff


def input_data_is_valid(last_semester_student_json_list, current_semester_student_json_list):
    if last_semester_student_json_list:
        if last_semester_student_json_list < current_semester_student_json_list:
            raise ValueError("len(last_semester_student_json_list) should larger than"
                             " len(current_semester_student_json_list)")
    elif not last_semester_student_json_list:
        raise ValueError("last_semester_student_json_list should not be [] or None")


def load_txt_file_to_json_list(file_path):
    if not file_path:
        return []
    try:
        file = open(file_path, 'r')
        row_data = file.readlines()
    except UnicodeDecodeError:
        file = open(file_path, 'r', encoding='utf-8')
        row_data = file.readlines()
    json_data_list = []
    dict_keys = []
    for line_no, line in enumerate(row_data):
        if line_no == 0:
            dict_keys = line.strip('\n').split('\t')
        else:
            dict_data = {}
            dict_values = line.strip('\n').split('\t')
            for i, dict_key in enumerate(dict_keys):
                dict_data[dict_key] = dict_values[i]
            json_data = json.dumps(dict_data)
            json_data_list.append(json_data)
    file.close()
    return json_data_list
