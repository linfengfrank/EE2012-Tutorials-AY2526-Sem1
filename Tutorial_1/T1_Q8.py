import math

n, r = 365, 23

nPr = math.perm(n, r)   # permutations: nPr

P= nPr / pow(n, r)

print("P =", P)

