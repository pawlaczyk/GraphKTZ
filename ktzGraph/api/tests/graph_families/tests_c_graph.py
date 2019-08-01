#coding=utf-8
from unittest.mock import Mock

import unittest

from ktzGraph.api.adjacency_matrix.implmentation.polynomial import EigenvaluesCalculator
from ktzGraph.api.graph_families.c_graph import CGraphChecker


class CGraphCheckerTest(unittest.TestCase):

    def test_check_is_c_graph_should_pass(self):

        eigenvalues_calculator = Mock()  # type: EigenvaluesCalculator
        eigenvalues_calculator.get_eigenvalues.return_value=[1.0, 1.0]

        c_graph_checker = CGraphChecker(eigenvalues_calculator)
        result = c_graph_checker.check_is_c_graph()

        self.assertTrue(result)


