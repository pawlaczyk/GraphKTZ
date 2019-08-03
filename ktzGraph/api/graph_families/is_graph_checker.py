# coding=utf-8
import numpy as np


class GraphCheckerError(Exception):
    """Exception for checking graph classes"""


class IsGraphChecker:
    def __init__(self, matrix:np.array)->bool:
        self.matrix = matrix

    def is_graph(self)->bool:
        """
        Macierz grafu:
        - wartości całkowite
        - kwadratowa
        - wartości większe od zera
        """
        try:
            non_integer_values = filter(lambda ele: issubclass(ele.dtype.type, np.integer), self.matrix.ravel())
            if list(non_integer_values):
                raise GraphCheckerError("Matrix contains non integers values.")

            if self.matrix.shape == (1,):
                if self.matrix[0] == 1:
                    return True  # K1 graph
                else:
                    raise GraphCheckerError("Graph Zero is not supported.")

            n, m = self.matrix.shape
            if n != m:
                raise GraphCheckerError("Matrix is not quadratic.")

            negative_elements = filter(lambda x: x is False, np.greater_equal(self.matrix, 0).ravel())
            if list(negative_elements):
                raise GraphCheckerError("Matrix contains negative values.")

        except AttributeError:
            raise GraphCheckerError("Matrix contains inappropriate values.")

        return True


class IsSimpleGraphChecker(IsGraphChecker):
    def is_simple(self)->bool:
        pass


class IsNonDirectedGraphChecker(IsSimpleGraphChecker):
    def is_non_directed(self):
        pass


class IsDirectedGraphChecker(IsSimpleGraphChecker):
    def is_directed(self):
        pass


class IsCyclicGraphChecker(IsSimpleGraphChecker):
    def is_cyclic(self):
        pass


class IsCirculantGraphChecker(IsSimpleGraphChecker):
    def is_circulant(self):
        pass
