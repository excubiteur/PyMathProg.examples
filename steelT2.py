from pymprog import *


def steelT2(PROD, WEEKS, rate, inv0, avail, market, prodcost, invcost, revenue):
    begin('steelT2')

    PROD_WEEKS = iprod(PROD, WEEKS)

    Make = var('Make', PROD_WEEKS)
    for i in PROD_WEEKS:
        Make[i] >= 0

    Inv = var('Inv', PROD_WEEKS)
    for i in PROD_WEEKS:
        Inv[i] >= 0

    Sell = var('Sell', PROD_WEEKS)
    for p, t in PROD_WEEKS:
        0 <= Sell[p, t] <= market[p][t]

    maximize(
        sum(
            (
                revenue[p][t] * Sell[p, t]
                - prodcost[p] * Make[p, t]
                - invcost[p] * Inv[p, t]
            )
            for p in PROD for t in WEEKS
        )
    )

    for t in WEEKS:
        sum((1 / rate[p]) * Make[p, t] for p in PROD) <= avail[t]

    for p in PROD:
        Make[p, 0] + inv0[p] == Sell[p, 0] + Inv[p, 0]

    for p in PROD:
        for t in WEEKS:
            if t > 0:
                Make[p, t] + Inv[p, t - 1] == Sell[p, t] + Inv[p, t]

    solve()


def main():
    PROD_set = ['band', 'coils']
    PROD = range(len(PROD_set))

    WEEKS_set = ['27sep', '04oct', '11oct', '18oct']
    WEEKS = range(len(WEEKS_set))

    avail = [40, 40, 32, 40]

    rate = [200, 140]
    inv0 = [10, 0]

    prodcost = [10, 11]
    invcost = [2.5, 3]

    revenue = [
        [25, 26, 27, 27],
        [30, 35, 37, 39]]

    market = [
        [6000, 6000, 4000, 6500],
        [4000, 2500, 3500, 4200]]

    steelT2(PROD, WEEKS, rate, inv0, avail, market, prodcost, invcost, revenue)
    assert (vobj() == 515033)


if __name__ == "__main__":
    main()
