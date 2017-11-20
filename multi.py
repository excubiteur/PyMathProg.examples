from pymprog import *


def multi(ORIG, DEST, PROD, supply, demand, limit, cost):
    begin('multi')

    ORIG_DEST_PROD = iprod(ORIG, DEST, PROD)

    Trans = var('Trans', ORIG_DEST_PROD)
    for i in ORIG_DEST_PROD:
        Trans[i] >= 0

    minimize(sum(cost[i][j][p] * Trans[i, j, p] for i in ORIG for j in DEST for p in PROD))

    for i in ORIG:
        for p in PROD:
            sum(Trans[i, j, p] for j in DEST) == supply[i][p]

    for j in DEST:
        for p in PROD:
            sum(Trans[i, j, p] for i in ORIG) == demand[j][p]

    for i in ORIG:
        for j in DEST:
            sum(Trans[i, j, p] for p in PROD) <= limit

    solve()


def main():
    ORIG_set = ['GARY', 'CLEV', 'PITT']
    ORIG = range(len(ORIG_set))

    DEST_set = ['FRA', 'DET', 'LAN', 'WIN', 'STL', 'FRE', 'LAF']
    DEST = range(len(DEST_set))

    PROD_set = ['band', 'coils', 'plate']
    PROD = range(len(PROD_set))

    # Numbers copied and pasted from multi.dat:
    transposed_supply = [
        [400, 700, 800],
        [800, 1600, 1800],
        [200, 300, 300]]

    supply = [list(x) for x in zip(*transposed_supply)]

    # Numbers copied and pasted from multi.dat:
    transposed_demand = [
        [300, 300, 100, 75, 650, 225, 250],
        [500, 750, 400, 250, 950, 850, 500],
        [100, 100, 0, 50, 200, 100, 250]]

    demand = [list(x) for x in zip(*transposed_demand)]

    # Numbers copied and pasted from multi.dat:
    bands = [
        [30, 10, 8, 10, 11, 71, 6],
        [22, 7, 10, 7, 21, 82, 13],
        [19, 11, 12, 10, 25, 83, 15]]
    coils = [
        [39, 14, 11, 14, 16, 82, 8],
        [27, 9, 12, 9, 26, 95, 17],
        [24, 14, 17, 13, 28, 99, 20]]
    plate = [
        [41, 15, 12, 16, 17, 86, 8],
        [29, 9, 13, 9, 28, 99, 18],
        [26, 14, 17, 13, 31, 104, 20]]

    cost = [[[bands[i][j], coils[i][j], plate[i][j]] for j in range(7)] for i in range(3)]

    limit = 625

    multi(ORIG, DEST, PROD, supply, demand, limit, cost)
    assert (vobj() == 199500)


if __name__ == "__main__":
    main()
