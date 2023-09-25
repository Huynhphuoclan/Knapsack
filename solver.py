from ortools.algorithms import pywrapknapsack_solver
import os
import time


def main():
    # dataset
    LV1_FOLDER_PATH = 'C:/Huynh_Lan/AI/Knapsack/kplib/12Circle'
    for file_path in sorted(os.listdir(f'{LV1_FOLDER_PATH}')):
        file = open(f'{LV1_FOLDER_PATH}/{file_path}')
        file.readline()
        n = int(file.readline().strip())
        capacity = int(file.readline().strip())
        file.readline()
        values = []
        weights = []
        capacities = [capacity]
        values.append(0)
        weights.append(0)
        for i in range(1, n+1):
            vi, wi = list(map(int, file.readline().split()))
            values.append(vi)
            weights.append(wi)

        # Create the solver.
        solver = pywrapknapsack_solver.KnapsackSolver(
            pywrapknapsack_solver.KnapsackSolver.
            KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

        weights = [weights]
        solver.set_time_limit(180)
        start = time.time()
        solver.Init(values, weights, capacities)
        computed_value = solver.Solve()

        packed_items = []
        packed_weights = []
        total_weight = 0
        print('\nn =', n)
        print('capacities =', capacity)
        print('Time = ', time.time()-start)
        print('Total value =', computed_value)
        for i in range(len(values)):
            if solver.BestSolutionContains(i):
                packed_items.append(i)
                packed_weights.append(weights[0][i])
                total_weight += weights[0][i]
        print('Total weight:', total_weight)
        print('Packed items:', packed_items)
        print('Packed_weights:', packed_weights)
        with open("C:/Huynh_Lan/AI/Knapsack/result/12Circle/Solver_result_n_" + str(i) + ".txt", 'w+') as solver_file:  # write results to file
            print('\nn =', n, file=solver_file)
            print('capacities =', capacity, file=solver_file)
            print('Time = ', time.time()-start, file=solver_file)
            print('Total value =', computed_value, file=solver_file)
            print('Total weight:', total_weight, file=solver_file)
            print('Packed items:', packed_items, file=solver_file)
            print('Packed_weights:', packed_weights, file=solver_file)
        file.close()


if __name__ == '__main__':
    main()
