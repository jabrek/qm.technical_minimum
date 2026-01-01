import numpy as np

# 1. Definiujemy bazę standardową (zwaną bazą Z)
# |0> = [1, 0], |1> = [0, 1]
ket0 = np.array([[1], [0]])
ket1 = np.array([[0], [1]])

# 2. Obliczamy iloczyny zewnętrzne (Outer Product) |i><i|
# W NumPy: ket @ bra (gdzie bra to ket.conj().T)
outer0 = ket0 @ ket0.conj().T
outer1 = ket1 @ ket1.conj().T

print("Projektor |0><0|:\n", outer0)
print("Projektor |1><1|:\n", outer1)

# 3. Sprawdzamy relację zupełności: sum( |i><i| ) == I
identity_check = outer0 + outer1
print("\nSuma (Relacja zupełności):\n", identity_check)

# 4. Sprawdźmy to samo dla innej bazy (np. bazy Hadamarda / bazy X)
# |+> = 1/sqrt(2) * (|0> + |1>)
# |-> = 1/sqrt(2) * (|0> - |1>)
plus = (1 / np.sqrt(2)) * (ket0 + ket1)
minus = (1 / np.sqrt(2)) * (ket0 - ket1)

outer_plus = plus @ plus.conj().T
outer_minus = minus @ minus.conj().T

print("\nSuma w bazie Hadamarda:\n", outer_plus + outer_minus)
