from pymprog import *


def steel4(PROD, STAGE, rate, profit, commit, market, avail):
    begin('steel4')

    Make = var('Make', PROD)
    for p in PROD:
        commit[p] <= Make[p] <= market[p]

    maximize(sum(profit[p] * Make[p] for p in PROD))

    for s in STAGE:
        sum((1 / rate[p][s]) * Make[p] for p in PROD) <= avail[s]

    solve()


def main():
    PROD_set = ['band', 'coils', 'plate']
    PROD = range(len(PROD_set))

    STAGE_set = ['reheat', 'roll']
    STAGE = range(len(STAGE_set))

    # Numbers copied and pasted from steel4.dat:
    transposed_params = [
        [25, 1000, 6000],
        [30, 500, 4000],
        [29, 750, 3500]]

    params = [list(x) for x in zip(*transposed_params)]

    profit = params[0]
    commit = params[1]
    market = params[2]

    rate = [
        [200, 200],
        [200, 140],
        [200, 160]]

    avail = [35, 40]

    steel4(PROD, STAGE, rate, profit, commit, market, avail)
    assert (round(vobj() * 10000) == 1900714286)


if __name__ == "__main__":
    main()
