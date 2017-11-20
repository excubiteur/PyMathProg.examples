from pymprog import *


def steel(PROD, rate, profit, market, avail):
    begin('steel')

    Make = var('Make', PROD)
    for p in PROD:
        0 <= Make[p] <= market[p]

    maximize(sum(profit[p] * Make[p] for p in PROD))

    sum((1 / rate[p]) * Make[p] for p in PROD) <= avail

    solve()


if __name__ == "__main__":
    PROD_set = ['band', 'coils']
    PROD = range(len(PROD_set))

    # Numbers copied and pasted from steel.dat:
    transposed_params = [
        [200, 25, 6000],
        [140, 30, 4000]]

    params = [list(x) for x in zip(*transposed_params)]

    rate = params[0]
    profit = params[1]
    market = params[2]
    avail = 40

    steel(PROD, rate, profit, market, avail)
    assert (vobj() == 192000)
