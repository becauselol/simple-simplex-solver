from src.linear_solver import Solver 


def main():

    c = [-3, -1, -2, 0, 0, 0]
    a = [
        [1, 1, 3, 1, 0, 0],
        [2, 2, 5, 0, 1, 0],
        [4, 1, 2, 0, 0, 1]
    ]
    b = [30, 24, 36]

    solver = Solver(c, a, b)

    solver.solve()
    
    solver.print_solution()


if __name__ == "__main__":
    main()
