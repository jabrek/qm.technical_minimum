import numpy as np

A = np.random.rand(2) + 1j * np.random.rand(2)

inner_product = np.vdot(A, A)
print(f"Inner product Imaginary: {inner_product.imag:.4f}")
print("Is inner product real?", np.isclose(inner_product.imag, 0.0))
