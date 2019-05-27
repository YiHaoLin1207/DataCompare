# -*- coding: utf-8 -*-


class FileHandler:
    @staticmethod
    def load_file_to_dict_list(file_path):
        try:
            file = open(file_path, 'r')
            row_data = file.readlines()
        except UnicodeDecodeError:
            file = open(file_path, 'r', encoding='utf-8')
            row_data = file.readlines()
        dict_data_list = []
        dict_keys = []
        for line_no, line in enumerate(row_data):
            if line_no == 0:
                dict_keys = line.strip('\n').split('\t')
            else:
                dict_data = {}
                dict_values = line.strip('\n').split('\t')
                for i, dict_key in enumerate(dict_keys):
                    dict_data[dict_key] = dict_values[i]
                dict_data_list.append(dict_data)
        file.close()

        return dict_data_list