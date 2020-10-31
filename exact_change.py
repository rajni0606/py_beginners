def exact_change(target_amount, L):
    if target_amount == 0:
        return True
    if len(L) == 0 or target_amount < 0:
        return False
    lose_it = exact_change(target_amount, L[1:])
    use_it = exact_change(target_amount - L[0], L[1:])
    return use_it or lose_it
assert exact_change(42, [25, 16, 2, 15]) == True
