from pymprog import *


def steel3(PROD, rate, profit, commit, market, avail):
    begin('steel3')

    Make = var('Make', PROD)
    for p in PROD:
        commit[p] <= Make[p] <= market[p]

    maximize(sum(profit[p] * Make[p] for p in PROD))

    sum((1 / rate[p]) * Make[p] for p in PROD) <= avail

    solve()


if __name__ == "__main__":
    PROD_set = ['band', 'coils', 'plate']
    PROD = range(len(PROD_set))

    # Numbers copied and pasted from steel3.dat:
    transposed_params = [
        [200, 25, 1000, 6000],
        [140, 30, 500, 4000],
        [160, 29, 750, 3500]]

    params = [list(x) for x in zip(*transposed_params)]

    rate = params[0]
    profit = params[1]
    commit = params[2]
    market = params[3]
    avail = 40

    steel3(PROD, rate, profit, commit, market, avail)
    assert (round(vobj() * 10000) == 1948285714)
