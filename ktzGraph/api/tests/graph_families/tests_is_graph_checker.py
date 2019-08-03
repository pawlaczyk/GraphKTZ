# coding=utf-8
import unittest
import numpy as np
from sympy import symbols

from ktzGraph.api.graph_families.is_graph_checker import IsGraphChecker, GraphCheckerError


class IsGraphCheckerTest(unittest.TestCase):
    def setUp(self):
        self.symbol = symbols('x')
        self.graph_zero = np.array([0])
        self.k1 = np.array([1])
        self.k2 = np.array([[0, 1], [1, 0]])

    def test_is_graph_proper_matrix_should_pass(self):
        matrix = np.array([[0,1], [1,0]])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertTrue(is_graph_checker.is_graph())

        is_graph_checker = IsGraphChecker(self.k1)
        self.assertTrue(is_graph_checker.is_graph())

    def test_is_graph_non_quadratic_matrix_should_not_pass(self):
        matrix = np.array([[0, 1, 0], [1, 0, 1]])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

        is_graph_checker = IsGraphChecker(self.graph_zero)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

    def test_is_graph_matrix_with_negative_number_should_not_pass(self):
        matrix = np.array([-1])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

        matrix = np.array([[-1, 0], [1, 0]])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

    def test_is_graph_matrix_with_non_integer_number_should_not_pass(self):
        matrix = np.array([1.1])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

        matrix = np.array([0.0])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

        matrix = np.array([0.000000000000000000000000000001])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

    def test_is_graph_with_unsupported_data_should_not_pass(self):
        matrix = np.array(["A"])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

        matrix = np.array(["\n"])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)

        matrix = np.array([None])
        is_graph_checker = IsGraphChecker(matrix)
        self.assertRaises(GraphCheckerError, is_graph_checker.is_graph)
