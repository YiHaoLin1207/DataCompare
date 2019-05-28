# -*- coding: utf-8 -*-
import json


def get_intersection_of_two_list(list_a, list_b):
    intersection = list(set(list_a).intersection(list_b))
    return intersection


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
