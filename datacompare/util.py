# -*- coding: utf-8 -*-
import json


def make_len_of_list_a_over_list_b(self, list_a, list_b):
    if len(list_a) >= len(list_b):
        pass
    else:
        temp_list = list_b
        list_b = list_a
        list_a = temp_list

def trans_json_list_to_dict_list(json_list_data):
    dict_list_data = []
    for json_data in json_list_data:
        dict_list_data.append(json.loads(json_data))
    return dict_list_data


def get_intersection_of_two_list(list_a, list_b):
    intersection = list(set(list_a).intersection(list_b))
    return intersection


def get_diff_of_two_list(list_a, list_b):
    if len(list_a) >= len(list_b):
        return list(set(list_a) - set(list_b))
    else:
        return list(set(list_b) - set(list_a))


def load_txt_file_to_json_list(file_path):
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
