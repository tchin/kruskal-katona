# main.py
import sys
import scipy.special


def compute_repr(n, k):
    if n == 0:
        return []
    if k == 1:
        return [(n, 1)]
    i = k
    while scipy.special.binom(i+1, k) <= n:
        i += 1
    return [(i, k)] + compute_repr(n - scipy.special.binom(i, k), k-1)

def compute_del_k(expansion):
    res = 0
    for e in expansion:
        res += int(scipy.special.binom(e[0], e[1]-1))
    return res

if __name__ == "__main__":
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    expansion = compute_repr(n,k)
    print(expansion)
    dl_k = compute_del_k(expansion)
    print(f'dl_{k}({n}) = {dl_k}')