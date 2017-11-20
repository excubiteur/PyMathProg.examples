from pymprog import *


def prod(P, a, b, c, u):
    begin('prod')

    X = var('X', P)

    maximize(sum(c[j] * X[j] for j in P))

    sum((1 / a[j]) * X[j] for j in P) <= b

    for j in P:
        0 <= X[j] <= u[j]

    solve()


def main():
    P_set = ['band', 'coils']
    P = range(len(P_set))

    # Numbers copied and pasted from prod.dat:
    transposed_params = [
        [200, 25, 6000],
        [140, 30, 4000]]

    params = [list(x) for x in zip(*transposed_params)]

    a = params[0]
    c = params[1]
    u = params[2]
    b = 40

    prod(P, a, b, c, u)
    assert (vobj() == 192000)

if __name__ == "__main__":
    main()