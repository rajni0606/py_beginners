def numsort(L):
    if not L:
        return L
    else:
        low = [min(L)]
        L.remove(min(L))
    return low + gensort(L)
assert numsort([42, 1, 3.14]) == [1, 3.14, 42]
