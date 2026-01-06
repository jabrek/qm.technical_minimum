# Suskind lectures - lecture 2, exercise 2.3
import numpy as np

alpha = 1 / np.sqrt(2)
beta = -1j / np.sqrt(2)  # faza 90 stopni - czysto urojona

# podpunkt a:
val_a = np.conj(alpha) * alpha
print("alpha*alpha* =", val_a)

# podpunkt b: alpha**beta + alpha*beta*
val_b = np.conj(alpha) * beta + alpha * np.conj(beta)
print("Suma alpha*beta + alpha beta* =", val_b)

# sprawdzmy alpha*beta
z = np.conj(alpha) * beta
print("alpha*beta =", z)
print(f"Purely imaginary? {np.isclose(z.real, 0.0)} ")
