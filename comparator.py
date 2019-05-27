#-*- coding: utf-8 -*-

from filehandler import FileHandler

class Comparator:
    @staticmethod
    def get_compared_result(file_path_1, file_path_2):
        data_1 = FileHandler.load_file_to_dict_list(file_path_1)
        data_2 = FileHandler.load_file_to_dict_list(file_path_2)
        for data1 in data_1:
            for data2 in data_2:
                if data1 == data2:
                    print(data1)



Comparator.get_compared_result('C:\\Users\\林一豪\\Desktop\\DataCompare\\sample\\107(2)校統1080515.txt',
                               'C:\\Users\\林一豪\\Desktop\\DataCompare\\sample\\108(1)減免名單(校統)1080527.txt')
