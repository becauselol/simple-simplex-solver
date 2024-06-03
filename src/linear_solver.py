class Tableau:
    def __init__(self, c, a, b):
        self.c = c
        self.a = a
        self.b = b
        self.soln = 0

    def can_improve(self):
        return any(val < 0 for val in self.c)

    def find_pivot(self, method="blands"):
        for i, val in enumerate(self.c):
            if val < 0:
                self.pivot_col = i
                break

        self.leaving_row = self.ratio_test(self.pivot_col, method)

        return self.pivot_col, self.leaving_row

    def get_value(self):
        return self.soln

    def get_solution(self):
        solution = [0] * len(self.c)
        for idx, tup in enumerate(zip(*self.a)):
            if tup.count(1) == 1 and tup.count(0) == len(self.b) - 1:
                soln_row = tup.index(1)
                solution[idx] = self.b[soln_row]

        return solution

    def print_tableau(self):
        str_c = [f"{val:>8.2f}" for val in self.c]
        print(f"{self.soln:>8.2f} | {", ".join(str_c)}")
        print("-" * (10*(len(str_c) + 1)))
        for i in range(len(self.b)):
            str_a = [f"{val:>8.2f}" for val in self.a[i]]
            print(f"{self.b[i]:>8.2f} | {", ".join(str_a)}")

    def ratio_test(self, col, method="blands"):
        min_ratio = None
        candidates = []
        for i in range(len(self.b)):
            
            # we need to skip any 0s
            if self.a[i][col] < 0:
                continue

            if self.a[i][col] == 0:
                raise Exception(f"Unbounded? A {col}, {i}, value is {self.a[i][col]}")
            ratio = self.b[i]/self.a[i][col]

            if not min_ratio:
                min_ratio = ratio
                candidates.append(i)
            elif ratio == min_ratio:
                candidates.append(i)
            elif ratio < min_ratio:
                min_ratio = ratio
                candidates = [i]


        if not candidates:
            raise Exception("Do we still need to pivot?")
        return candidates[0]

    def pivot(self, verbose=False):
        col, row = self.find_pivot()

        if verbose:
            print(f"Pivoting using Row {row + 1}, Col {col + 1}")

        # now we make the values in self.a[col][row] = 1
        # while also making sure the rest in the row are multiplied accordingly

        if self.a[row][col] != 1:
            divisor = self.a[row][col]
            for j in range(len(self.a[row])):
                self.a[row][j] /= divisor

            self.b[row] /= divisor

        # now make the other rows for that column be 0
        # we do so by row operations

        for i in range(len(self.a)):
            if i == row:
                continue

            if self.a[i][col] != 0:
                multiplier = self.a[i][col]

                for j in range(len(self.a[i])):
                    self.a[i][j] -= (multiplier * self.a[row][j])
                
                self.b[i] -= (multiplier * self.b[row])

        # we also need to do this to c
        multiplier = self.c[col]
        for i in range(len(self.c)):
            self.c[i] -= (multiplier * self.a[row][i])

        # lastly for the solution
        self.soln -= (multiplier * self.b[row])
        


class Solver:
    def __init__(self, cost_vec, a_vec, b_vec, max=True) -> None:
        self.validate_inputs(cost_vec, a_vec, b_vec)
        self.c = cost_vec
        self.a = a_vec
        self.b = b_vec
        self.max = max

    def solve(self, verbose=False, print_iter=False):
        iter = 1
        tableau = Tableau(self.c, self.a, self.b)

        while tableau.can_improve():
            if verbose or print_iter:
                print(f"Iteration: {iter}")
            tableau.pivot(verbose)
            iter += 1
            if verbose:
                tableau.print_tableau()

        self.obj_value = tableau.get_value()
        self.obj_soln = tableau.get_solution()

    def print_solution(self):
        print(f"Objective Value is {self.obj_value}")
        print(f"Solution is {self.obj_soln}")

    def validate_inputs(self, c, a, b):
        if len(c) <= 0:
            raise Exception("cost vector length not larger than 0")

        if len(a) <= 0:
            raise Exception("a matrix length not larger than 0")

        if type(a[0]) != list:
            raise Exception("a is not 2D")

        if len(a[0]) <= 0:
            raise Exception("a matrix length not larger than 0")

        # check size consistency
        a_size = len(a[0])
        for arr in a:
            if len(arr) != a_size:
                raise Exception("Inconsistent dimensions for A matrix")

        if len(b) <= 0:
            raise Exception("b vector length not larger than 0")

        if len(b) != len(a):
            raise Exception("A and b dimensions do not match")

        if len(c) != len(a[0]):
            raise Exception("A and c dimensions do not match")

        for i, val in enumerate(c):
            if not (type(val) is int or type(val) is float):
                raise Exception(f"item {i} in c vec not int or float")

        for i, val in enumerate(b):
            if not (type(val) is int or type(val) is float):
                raise Exception(f"item {i} in b vec not int or float")

        for i, arr in enumerate(a):
            for j, val in enumerate(arr):
                if not (type(val) is int or type(val) is float):
                    raise Exception(f"item {i}, {j} in A matrix not int or float")
