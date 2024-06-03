from src.linear_solver import Solver

def test_basic_case():
    # This is a test of equality
    
    c = [-10, -12, -12, 0, 0, 0]
    a = [
        [1, 2, 2, 1, 0, 0],
        [2, 1, 2, 0, 1, 0],
        [2, 2, 1, 0, 0, 1]
    ]
    b = [20, 20, 20]

    solver = Solver(c, a, b)
    solver.solve()
    assert(solver.obj_value == 136)
    assert(solver.obj_soln == [4, 4, 4, 0, 0, 0])

def test_another_case():

    c = [-3, -1, -2, 0, 0, 0]
    a = [
        [1, 1, 3, 1, 0, 0],
        [2, 2, 5, 0, 1, 0],
        [4, 1, 2, 0, 0, 1]
    ]
    b = [30, 24, 36]

    solver = Solver(c, a, b)
    solver.solve()
    assert(solver.obj_value == 28)
    assert(solver.obj_soln == [8, 4, 0, 18, 0, 0])

def test_cycling():

    c = [-10, 57, -9, 24, 0, 0, 0]
    a = [
        [0.5, -5.5, -2.5, 9, 1, 0, 0],
        [0.5, -1.5, -0.5, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1]
    ]
    b = [0, 0, 1]
    # need to figure out what this test is for

# chatGPT
# import unittest
#
# from simplex_solver import SimplexSolver
#
# class TestSimplexSolver(unittest.TestCase):
#
#     def test_minimization(self):
#         # Test minimization problem
#         c = [3, 2]
#         A = [[-2, 1], [1, 1]]
#         b = [4, 6]
#         solver = SimplexSolver(c, A, b)
#         solution = solver.solve()
#         self.assertAlmostEqual(solution['objective'], 10)
#         self.assertAlmostEqual(solution['x'], [2, 2])
#
#     def test_infeasible(self):
#         # Test infeasible problem
#         c = [1, 1]
#         A = [[-1, 1], [1, -1]]
#         b = [1, -1]
#         solver = SimplexSolver(c, A, b)
#         with self.assertRaises(ValueError):
#             solver.solve()
#
#     def test_unbounded(self):
#         # Test unbounded problem
#         c = [1, -1]
#         A = [[-1, 1], [1, -1]]
#         b = [1, 1]
#         solver = SimplexSolver(c, A, b)
#         with self.assertRaises(ValueError):
#             solver.solve()
#
#     def test_degeneracy(self):
#         # Test degeneracy
#         c = [2, 3, -4]
#         A = [[-2, 1, 1], [1, 2, 1], [3, 1, 2]]
#         b = [4, 6, 18]
#         solver = SimplexSolver(c, A, b)
#         solution = solver.solve()
#         self.assertAlmostEqual(solution['objective'], 10)
#         self.assertAlmostEqual(solution['x'], [0, 4, 0])
#
# if __name__ == '__main__':
#     unittest.main()
