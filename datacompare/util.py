# -*- coding: utf-8 -*-
import json
import codecs


def swap(list_a, list_b):
    temp_list = list_b
    list_b = list_a
    list_a = temp_list
    return list_a, list_b


def trans_dict_list_to_json_list(dict_list_data):
    if not dict_list_data:
        return []
    json_list_data = []
    for dict_data in dict_list_data:
        json_list_data.append(json.dumps(dict_data))
    return json_list_data


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
    if not list_a and not list_b:
        return []
    diff = list(set(list_a) - set(list_b))
    diff = [x for x in list_a if x in diff]
    return diff

def filter_student_list_with_dict_key(json_list):
    dict_list = trans_json_list_to_dict_list(json_list)
    new_dict_list = []
    for d in dict_list:
        new_dict = {k: v for k, v in d.items() if k in ['std_name', 'std_idno']}
        new_dict_list.append(new_dict)
    new_json_list = trans_dict_list_to_json_list(new_dict_list)
    return new_json_list


def load_txt_file_to_json_list(file_path):
    if not file_path:
        return []

    file = codecs.open(file_path, 'r', encoding='big5', errors='replace')
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


