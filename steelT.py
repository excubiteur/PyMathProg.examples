from pymprog import *


def steelT(PROD, T, rate, inv0, avail, market, prodcost, invcost, revenue):
    begin('steelT')

    PROD_1T = iprod(PROD, range(1, T + 1))
    PROD_0T = iprod(PROD, range(T + 1))

    Make = var('Make', PROD_1T)
    for i in PROD_1T:
        Make[i] >= 0

    Inv = var('Inv', PROD_0T)
    for i in PROD_0T:
        Inv[i] >= 0

    Sell = var('Sell', PROD_1T)
    for p, t in PROD_1T:
        0 <= Sell[p, t] <= market[p][t]

    maximize(
        sum(
            (
                revenue[p][t] * Sell[p, t]
                - prodcost[p] * Make[p, t]
                - invcost[p] * Inv[p, t]
            )
            for p in PROD for t in range(1, T + 1)
        )
    )

    for t in range(1, T + 1):
        sum((1 / rate[p]) * Make[p, t] for p in PROD) <= avail[t]

    for p in PROD:
        Inv[p, 0] == inv0[p]

    for p in PROD:
        for t in range(1, T + 1):
            Make[p, t] + Inv[p, t - 1] == Sell[p, t] + Inv[p, t]

    solve()


def main():
    PROD_set = ['band', 'coils']
    PROD = range(len(PROD_set))

    T = 4

    avail = [0, 40, 40, 32, 40]

    rate = [200, 140]
    inv0 = [10, 0]

    prodcost = [10, 11]
    invcost = [2.5, 3]

    revenue = [
        [0, 25, 26, 27, 27],
        [0, 30, 35, 37, 39]]

    market = [
        [0, 6000, 6000, 4000, 6500],
        [0, 4000, 2500, 3500, 4200]]

    steelT(PROD, T, rate, inv0, avail, market, prodcost, invcost, revenue)
    assert (vobj() == 515033)


if __name__ == "__main__":
    main()
