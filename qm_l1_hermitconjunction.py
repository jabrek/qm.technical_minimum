import numpy as np

A = np.array([[2 + 1j], [2 - 1j]])

A_hermit = np.conj(A).T

print("A\n", A)
print("Type of A:", type(A))
print("A_hermit:\n", A_hermit)
# print type of A_hermit
print("Type of A_hermit:", type(A_hermit))
print(
    "hermit product A_hermit * A:\n", A_hermit @ A
)  # using @ operator for matrix multiplication
print(
    "hermit product A_hermit * A (using np.dot):\n", np.vdot(A_hermit, A)
)  # using np.dot for matrix multiplication
