# coding=utf-8
"""
TODO: jak przedstawić graf o pyustym zbiorze wierzchołków? inna reprezentacja grafu niż macierz sąsiedztwa?
"""
import numpy as np


class GraphCheckerError(Exception):
    """Exception for checking graph families"""

class GraphNotImpementedError(NotImplementedError):
    """Exception for not supported familes of graph"""


class GraphCheckerBase:
    def __init__(self, matrix:np.array):
        self.matrix = matrix

    def check(self):
        pass


class IsGraphChecker(GraphCheckerBase):
    def check(self)->bool:
        """
        Macierz grafu:
        - wartości całkowite
        - kwadratowa
        - wartości większe od zera
        @note: Wyjątek grafy o n=1
        """
        def check_is_numpy_integer(ele):
            if issubclass(ele.dtype.type, np.int64):
                return True
            if issubclass(ele.dtype.type, np.int32):
                return True
            return False

        try:
            non_integer_values = filter(lambda ele: not check_is_numpy_integer(ele), self.matrix.ravel())
            if list(non_integer_values):
                raise GraphCheckerError("Matrix contains non integers values.")

            if not np.count_nonzero(self.matrix):
                raise GraphCheckerError("Graph Zero is not supported.")

            if self.matrix.shape == (1,):
                if np.greater_equal(self.matrix, 1):
                    return True  # K1 or cycle
                raise GraphCheckerError("Zero graph is not supported.")

            n, m = self.matrix.shape or (self.matrix.shape, None)
            if n != m:
                raise GraphCheckerError("Matrix is not quadratic.")

            negative_elements = filter(lambda x: x, np.less(self.matrix, 0).ravel())
            if list(negative_elements):
                raise GraphCheckerError("Matrix contains negative values.")

        except AttributeError:
            raise GraphCheckerError("Matrix contains inappropriate values.")

        return True


class IsSimpleGraphChecker(IsGraphChecker):
    def check(self)->bool:
        """
        Macierz grafu prostego:
        - binarna
        - zera na głównej przekątnej
        - zbiór wierzchołków niepusty V(G)
        - E(G) zbiór krawędzie może być pusty

        @note: wyjątek graf K1
        """
        super(IsSimpleGraphChecker, self).check()

        if not np.array_equal(self.matrix, self.matrix.astype(bool)):
            return False

        if self.matrix.shape == (1,):
            return True  # K1 or cycle albo od razu budować graf K1?

        if list(filter(lambda x: np.not_equal(x, 0), self.matrix.diagonal())):
            return False

        return True


class IsNonDirectedGraphChecker(IsSimpleGraphChecker):
    def check(self)->bool:
        """
        Dla grafów nieskierowanych macierz sąsiedztwa jest z definicji symetryczna
        """
        return np.allclose(self.matrix, self.matrix.T)  # checks is symmetric


class IsDirectedGraphChecker(IsSimpleGraphChecker):
    def check(self)->bool:
        pass


class IsCyclicGraphChecker(IsSimpleGraphChecker):
    def check(self)->bool:
        pass


class IsCirculantGraphChecker(IsSimpleGraphChecker):
    def check(self)->bool:
        pass
