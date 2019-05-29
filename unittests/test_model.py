# -*- coding: utf-8 -*-

from datacompare.model import StudentList
import json
import unittest


class TestStudentList(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()
        self.last_semester_student_json_list = [json.dumps('student1'),
                                                json.dumps('student2'),
                                                json.dumps('student3')]
        self.current_semester_student_json_list = [json.dumps('student1'),
                                                   json.dumps('student2'),
                                                   json.dumps('student5')]

    def test_get_finished_older_student(self):
        finished_older_student = self.student_list.get_finished_older_student(self.last_semester_student_json_list,
                                                                              self.current_semester_student_json_list)
        self.assertEqual(finished_older_student, [json.dumps('student1'), json.dumps('student2')])

        missing_one_param_list = self.student_list.get_finished_older_student(self.current_semester_student_json_list,
                                                                              [])
        self.assertEqual(missing_one_param_list, [])

    def test_get_unfinished_older_student(self):
        unfinished_older_student = self.student_list.get_unfinished_older_student(self.last_semester_student_json_list,
                                                                                  self.current_semester_student_json_list)
        self.assertEqual(unfinished_older_student, [json.dumps('student3')])

        missing_one_param_list = self.student_list.get_unfinished_older_student(self.last_semester_student_json_list,
                                                                                [])
        self.assertEqual(missing_one_param_list, [json.dumps('student1'),
                                                  json.dumps('student2'),
                                                  json.dumps('student3')])

    def test_get_new_student(self):
        new_student = self.student_list.get_new_student(self.last_semester_student_json_list,
                                                        self.current_semester_student_json_list)
        self.assertEqual(new_student, [json.dumps('student5')])

        missing_one_param_list = self.student_list.get_new_student(self.last_semester_student_json_list,
                                                                   [])
        self.assertEqual(missing_one_param_list, [])

    def test_get_all_unfinished_student(self):
        all_unfinished_student = self.student_list.get_all_unfinished_student(self.last_semester_student_json_list,
                                                                              self.current_semester_student_json_list)
        self.assertEqual(all_unfinished_student, ['student3', 'student5'])

        missing_one_param_list = self.student_list.get_all_unfinished_student(self.last_semester_student_json_list,
                                                                              [])
        self.assertEqual(missing_one_param_list, ['student1',
                                                  'student2',
                                                  'student3'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
