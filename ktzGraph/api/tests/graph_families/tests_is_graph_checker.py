# coding=utf-8
import unittest
import mock
import numpy as np

from ktzGraph.api.graph_families.is_graph_checker import IsGraphChecker, GraphCheckerError, IsSimpleGraphChecker


class IsGraphCheckerTest(unittest.TestCase):
    def setUp(self):
        self.graph_zero = np.array([0])
        self.k1 = np.array([1])
        self.k2 = np.array([[0, 1], [1, 0]])
        self.zero_matrix = np.zeros((2, 2))

    def test_check_proper_matrix_should_pass(self):
        is_graph_checker = IsGraphChecker(self.k1)
        print(is_graph_checker.check())
        self.assertTrue(is_graph_checker.check())

        matrix = np.array([[0,1], [1,0]])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertTrue(is_graph_checker.check())

    def test_check_non_quadratic_matrix_should_not_pass(self):
        matrix = np.array([[0, 1, 0], [1, 0, 1]])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

        is_graph_checker = IsGraphChecker(self.graph_zero)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

    def test_check_matrix_with_negative_number_should_not_pass(self):
        matrix = np.array([-1])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

        matrix = np.array([[-1, 0], [1, 0]])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

    def test_check_matrix_with_non_integer_number_should_not_pass(self):
        matrix = np.array([1.1])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

        matrix = np.array([0.0])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

        matrix = np.array([0.000000000000000000000000000001])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

    def test_check_with_zero_matrix(self):
        is_graph_checker = IsGraphChecker(self.zero_matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

    def test_check_with_unsupported_data_should_not_pass(self):
        matrix = np.array(["A"])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

        matrix = np.array(["\n"])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)

        matrix = np.array([None])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.check)


class IsSimpleGraphCheckerTest(unittest.TestCase):
    def setUp(self):
        self.graph_zero = np.array([0])
        self.k1 = np.array([1])
        self.k2 = np.array([[0, 1], [1, 0]])
        self.zero_matrix = np.zeros((2, 2))

    @mock.patch("ktzGraph.api.graph_families.is_graph_checker.IsGraphChecker.check")
    def test_check_with_binary_matrix_should_pass(self, mocked_super):
        """Mockowanie klasy bazowej"""
        simple_graph_checker = IsSimpleGraphChecker(self.graph_zero)
        self.assertTrue(simple_graph_checker.check())

        simple_graph_checker = IsSimpleGraphChecker(self.k1)
        self.assertTrue(simple_graph_checker.check())

        simple_graph_checker = IsSimpleGraphChecker(self.k2)
        self.assertTrue(simple_graph_checker.check())

    @mock.patch("ktzGraph.api.graph_families.is_graph_checker.IsGraphChecker.check")
    def test_check_with_values_on_diagonal_matrix_should_pass(self, mocked_super):
        matrix = np.array([[0, 1], [0, 1]])
        simple_graph_checker = IsSimpleGraphChecker(matrix)
        self.assertFalse(simple_graph_checker.check())

    @mock.patch("ktzGraph.api.graph_families.is_graph_checker.IsGraphChecker.check")
    def test_check_with_values_on_diagonal_matrix_should_pass(self, mocked_super):
        matrix = np.array([[0, 1], [0, 1]])
        simple_graph_checker = IsSimpleGraphChecker(matrix)
        self.assertFalse(simple_graph_checker.check())

        matrix = np.array([[1, 1], [1, 2]])
        simple_graph_checker = IsSimpleGraphChecker(matrix)
        self.assertFalse(simple_graph_checker.check())
