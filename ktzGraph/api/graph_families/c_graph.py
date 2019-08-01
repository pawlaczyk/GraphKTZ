#coding utf-8
from ktzGraph.api.adjacency_matrix.implmentation.polynomial import EigenvaluesCalculator
from ktzGraph.api.graph_families.abstract_graph_checker import AbstractGraphChecker


class CGraphChecker(AbstractGraphChecker):
    def __init__(self, eigenvaluesCalculator: EigenvaluesCalculator)->None:
        self.eigenvaluesCalculator = eigenvaluesCalculator

    def check_is_c_graph(self)->bool:
        """Sprawdzanie czy graf jest całkowity NIE MYLI Z GRAFEM PEŁNYM"""

        USp = self.eigenvaluesCalculator.get_eigenvalues()
        for i in USp:
            if isinstance(i, complex):
                return False
            if int(i) != i:
                return False
        return True
