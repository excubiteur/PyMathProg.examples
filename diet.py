from pymprog import *


def diet(FOOD, NUTR, cost, f_min, f_max, n_min, n_max, amt):
    begin('prod')

    Buy = var('Buy', FOOD)
    for j in FOOD:
        f_min[j] <= Buy[j] <= f_max[j]

    minimize(sum(cost[j] * Buy[j] for j in FOOD))

    for i in NUTR:
        n_min[i] <= sum(amt[i][j] * Buy[j] for j in FOOD) <= n_max[i]

    solve()


def main():
    NUTR_set = ['A', 'B1', 'B2', 'C']
    NUTR = range(len(NUTR_set))

    FOOD_set = ['BEEF', 'CHK', 'FISH', 'HAM', 'MCH', 'MTL', 'SPG', 'TUR']
    FOOD = range(len(FOOD_set))

    # Numbers copied and pasted from diet.dat:
    transposed_params1 = [
        [3.19, 0, 100],
        [2.59, 0, 100],
        [2.29, 0, 100],
        [2.89, 0, 100],
        [1.89, 0, 100],
        [1.99, 0, 100],
        [1.99, 0, 100],
        [2.49, 0, 100]]

    params1 = [list(x) for x in zip(*transposed_params1)]

    cost = params1[0]
    f_min = params1[1]
    f_max = params1[2]

    # Numbers copied and pasted from diet.dat:
    transposed_params2 = [
        [700, 10000],
        [700, 10000],
        [700, 10000],
        [700, 10000]]

    params2 = [list(x) for x in zip(*transposed_params2)]

    n_min = params2[0]
    n_max = params2[1]

    # Numbers copied and pasted from diet.dat:
    transposed_params3 = [
        [60, 20, 10, 15],
        [8, 0, 20, 20],
        [8, 10, 15, 10],
        [40, 40, 35, 10],
        [15, 35, 15, 15],
        [70, 30, 15, 15],
        [25, 50, 25, 15],
        [60, 20, 15, 10]]

    amt = [list(x) for x in zip(*transposed_params3)]

    diet(FOOD, NUTR, cost, f_min, f_max, n_min, n_max, amt)
    assert (vobj() * 10 == 882)


if __name__ == "__main__":
    main()
