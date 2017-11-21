from pymprog import *


def steelP(ORIG, DEST, PROD, rate, avail, demand, make_cost, trans_cost):
    begin('steelP')

    ORIG_DEST_PROD = iprod(ORIG, DEST, PROD)
    ORIG_PROD = iprod(ORIG, PROD)

    Make = var('Make', ORIG_PROD)
    Trans = var('Trans', ORIG_DEST_PROD)

    minimize(
        sum(make_cost[i][p] * Make[i, p] for i in ORIG for p in PROD)
        +
        sum(trans_cost[i][j][p] * Trans[i, j, p] for i in ORIG for j in DEST for p in PROD)
    )

    for i in ORIG:
        sum((1 / rate[i][p]) * Make[i, p] for p in PROD) <= avail[i]

    for i in ORIG:
        for p in PROD:
            sum(Trans[i, j, p] for j in DEST) == Make[i, p]

    for j in DEST:
        for p in PROD:
            sum(Trans[i, j, p] for i in ORIG) == demand[j][p]

    solve()


def main():
    ORIG_set = ['GARY', 'CLEV', 'PITT']
    ORIG = range(len(ORIG_set))

    DEST_set = ['FRA', 'DET', 'LAN', 'WIN', 'STL', 'FRE', 'LAF']
    DEST = range(len(DEST_set))

    PROD_set = ['band', 'coils', 'plate']
    PROD = range(len(PROD_set))

    # Numbers copied and pasted from steelP.dat:
    transposed_demand = [
        [300, 300, 100, 75, 650, 225, 250],
        [500, 750, 400, 250, 950, 850, 500],
        [100, 100, 0, 50, 200, 100, 250]]

    demand = [list(x) for x in zip(*transposed_demand)]

    # Numbers copied and pasted from steelP.dat:
    transposed_rate = [
        [200, 190, 230],
        [140, 130, 160],
        [160, 160, 170]]

    rate = [list(x) for x in zip(*transposed_rate)]

    # Numbers copied and pasted from steelP.dat:
    transposed_make_cost = [
        [180, 190, 190],
        [170, 170, 180],
        [180, 185, 185]]

    make_cost = [list(x) for x in zip(*transposed_make_cost)]

    # Numbers copied and pasted from steelP.dat:
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

    avail = [20, 15, 20]

    trans_cost = [[[bands[i][j], coils[i][j], plate[i][j]] for j in DEST] for i in ORIG]

    steelP(ORIG, DEST, PROD, rate, avail, demand, make_cost, trans_cost)
    assert (round(vobj()) == 1392175)


if __name__ == "__main__":
    main()
