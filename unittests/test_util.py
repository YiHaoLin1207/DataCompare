# -*- coding: utf-8 -*-

from datacompare.util import make_len_of_list_a_over_list_b
from datacompare.util import get_intersection_of_two_list
from datacompare.util import get_diff_of_two_list

import unittest

class TestUtil(unittest.TestCase):

    def setUp(self):
        self.list_a = ['c', 'b', 'a', 'e']
        self.list_b = ['a', 'b', 'c', 'd', 'f']

    def test_make_len_of_list_a_over_list_b(self):
        self.list_a, self.list_b = make_len_of_list_a_over_list_b(self.list_a, self.list_b)
        self.assertEqual(self.list_a, ['a', 'b', 'c', 'd', 'f'])

    def test_intersection_of_two_list(self):
        intersection_of_two_list = get_intersection_of_two_list(self.list_a, self.list_b)
        self.assertEqual(intersection_of_two_list, ['c', 'b', 'a'])

    def test_diff_of_two_list(self):
        diff_of_two_list = get_diff_of_two_list(self.list_a, self.list_b)
        self.assertEqual(diff_of_two_list, ['e'])

    def test_get_new_student(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
