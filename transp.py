from pymprog import *


def transp(ORIG, DEST, supply, demand, cost):
    begin('transp')

    ORIG_DEST = iprod(ORIG, DEST)

    Trans = var('Trans', ORIG_DEST)
    for i in ORIG_DEST:
        Trans[i] >= 0

    minimize(sum(cost[i][j] * Trans[i, j] for i in ORIG for j in DEST))

    for i in ORIG:
        sum(Trans[i, j] for j in DEST) == supply[i]

    for j in DEST:
        sum(Trans[i, j] for i in ORIG) == demand[j]

    solve()


def main():
    ORIG_set = ['GARY', 'CLEV', 'PITT']
    ORIG = range(len(ORIG_set))

    DEST_set = ['FRA', 'DET', 'LAN', 'WIN', 'STL', 'FRE', 'LAF']
    DEST = range(len(DEST_set))

    supply = [1400, 2600, 2900]
    demand = [900, 1200, 600, 400, 1700, 1100, 1000]

    cost = [
        [39, 14, 11, 14, 16, 82, 8],
        [27, 9, 12, 9, 26, 95, 17],
        [24, 14, 17, 13, 28, 99, 20]]

    transp(ORIG, DEST, supply, demand, cost)
    assert (vobj() == 196200)


if __name__ == "__main__":
    main()
