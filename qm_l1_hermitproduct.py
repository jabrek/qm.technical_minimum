import numpy as np

# Definiujemy trzy losowe wektory stanu (np. w przestrzeni 2D - jeden qubit)
A = np.array([1 + 2j, 3 - 1j])
B = np.array([4 + 0j, 2 + 2j])
C = np.array([1 - 2j, 3 - 1j])

# W NumPy np.vdot(x, y) oblicza iloczyn skalarny, automatycznie
# sprzęgając pierwszy argument (bra), co idealnie odwzorowuje <x|y>

lhs = np.vdot(A + B, C)
rhs = np.vdot(A, C) + np.vdot(B, C)
print("Lewa strona (A+B)|C>:", lhs)
print("Prawa strona <A|C> + <B|C>:", rhs)
print("Równość zachodzi:", np.allclose(lhs, rhs))
