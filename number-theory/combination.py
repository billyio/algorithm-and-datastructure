# https://note.nkmk.me/python-math-factorial-permutations-combinations/

# c = n! / (r! * (n - r)!)
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))