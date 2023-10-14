x = 3

var1 = x * x
var2 = var1 * x
var3 = var2 + x
out = var3 + 5

S = [1, x, out, var1, var2, var3]

l_1 = [0 if i != 1 else 1 for i in range(len(S))]
r_1 = l_1
o_1 = [0 if i != 3 else 1 for i in range(len(S))]

l_2 = [0 if i != 3 else 1 for i in range(len(S))]
r_2 = l_1
o_2 = [0 if i != 4 else 1 for i in range(len(S))]

l_3 = [int(i == var2 or i == x) for i in S]
r_3 = [1] + [0] * (len(S) - 1)
o_3 = [0 if i != 5 else 1 for i in range(len(S))]

l_4 = [S[0] * 5 if i == 0 else 0 if i != 5 else 1 for i in range(len(S))]
r_4 = [1] + [0] * (len(S) - 1)
o_4 = [0 if i != 2 else 1 for i in range(len(S))]

print("Gate 1:")
print("l_1:", l_1)
print("r_1:", r_1)
print("o_1:", o_1)
print("")
print("Gate 2:")
print("l_2:", l_2)
print("r_2:", r_2)
print("o_2:", o_2)
print("")
print("Gate 3:")
print("l_3:", l_3)
print("r_3:", r_3)
print("o_3:", o_3)
print("")
print("Gate 4:")
print("l_4:", l_4)
print("r_4:", r_4)
print("o_4:", o_4)
print("")

print("R1CS:")
print("")

print("L:")
L = [[l_1], [l_2], [l_3], [l_4]]
for sublist in L:
    print(sublist)

print("")
print("R:")
R = [[r_1], [r_2], [r_3], [r_4]]
for sublist in R:
    print(sublist)

print("")
print("O:")
O = [[o_1], [o_2], [o_3], [o_4]]
for sublist in O:
    print(sublist)

print("")
print("R1CS to QAP:")
print("")

# Interpolation:

import numpy as np
import sympy as sym

for z in range (0, len(S)):
    l_s = [l_1[z], l_2[z], l_3[z], l_4[z]]
    r_s = [r_1[z], r_2[z], r_3[z], r_4[z]]
    o_s = [o_1[z], o_2[z], o_3[z], o_4[z]]

    li = [l_s, r_s, o_s]

    print("------------------------------------")
    print("Round number", z+1, ":")

    for c in li:

        # Inputs:

        xi = np.array([1, 2, 3, 4]) # x-coordinates of the points
        fi = np.array(c) # y-coordinates of the points

        # Procedure:

        n = len(xi)
        x = sym.Symbol('x')
        pol = 0
        for i in range(0,n,1):
            num = 1
            den = 1
            for j in range(0,n,1):
                if (i!=j):
                    num = num*(x-xi[j])
                    den = den*(xi[i]-xi[j])
                t = (num/den)*fi[i]
            pol = pol + t
        polisimple = sym.expand(pol)

        # Output:

        print(polisimple)
