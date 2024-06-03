class Solver:
    def __init__(self, cost_vec, a_vec, b_vec) -> None:
        self.validate_inputs(cost_vec, a_vec, b_vec)
        self.c = cost_vec
        self.a = a_vec
        self.b = b_vec

    def solve(self):
        pass

    def validate_inputs(self, c, a, b):
        if len(c) <= 0:
            raise Error("cost vector length not larger than 0")

        if len(a) <= 0:
            raise Error("a matrix length not larger than 0")

        if type(a[0]) != list:
            raise Error("a is not 2D")

        if len(a[0]) <= 0:
            raise Error("a matrix length not larger than 0")

        # check size consistency
        a_size = len(a[0])
        for arr in a:
            if len(arr) != a_size:
                raise Error("Inconsistent dimensions for A matrix")

        if len(b) <= 0:
            raise Error("b vector length not larger than 0")

        if len(b) != len(a):
            raise Error("A and b dimensions do not match")

        if len(c) != len(a[0]):
            raise Error("A and c dimensions do not match")

        for i, val in enumerate(c):
            if type(val) != int or type(val) != float:
                raise Error(f"item {i} in c vec not int or float")

        for i, val in enumerate(b):
            if type(val) != int or type(val) != float:
                raise Error(f"item {i} in b vec not int or float")

        for i, arr in enumerate(a):
            for j, val in enumerate(arr):
                if type(val) != int or type(val) != float:
                    raise Error(f"item {i}, {j} in A matrix not int or float")



