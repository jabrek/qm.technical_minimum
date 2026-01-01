# define ket psi = 1/sqrt(2), 1/sqrt(2)
# calculate its outer product with itself
# project onto another ket phi = 1, 0 and print the result
import numpy as np

psi = np.array([1 / np.sqrt(2), 1 / np.sqrt(2)])
phi = np.array([1, 0])

print("Ket psi:", psi)
print("Bra psi (conjugate transpose):", np.conj(psi).T)
print("Ket phi:", phi)
print("Bra phi (conjugate transpose):", np.conj(phi).T)

# calculate outer product of psi with itself
projector = np.outer(psi, np.conj(psi))
print("Outer product of psi with itself (projector):")
print(projector)

# project onto another ket phi
# projected = np.dot(phi, projector)
projected = projector @ phi
print("Projection onto phi:")
print(projected)
