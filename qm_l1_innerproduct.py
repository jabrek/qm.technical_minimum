# define two kets - phi and psi
# calculate their inner product
# calculate probability of transition between the two states

import numpy as np

# define two kets
psi = np.array([1, 1j])
phi = np.array([0, 1])

print("Ket phi:", phi)
print("Ket psi:", psi)

# calculate their inner product
inner_product = np.vdot(phi, psi)
inner_product2 = np.conj(phi).dot(psi)
inner_product3 = phi.conj().T @ psi
# calculate probability of transition between the two states
prob_transition = abs(inner_product) ** 2

print("Inner product:", inner_product)
print("Inner product 2:", inner_product2)
print("Inner product 3:", inner_product3)
print("Probability of transition:", prob_transition)
