import numpy as np


def complex_gram_schmidt(vectors):
    """
    Algorytm ortogonalizacji dla zespolonej przestrzeni Hilberta.
    """
    basis = []
    for v in vectors:
        # v to nasz wektor 'v_k' (ket)
        # b to dotychczasowe wektory bazy 'u_j' (bra/ket)

        # Obliczamy rzuty wykorzystując np.vdot dla poprawnego sprzężenia bra
        projection = sum((np.dot(b, v) / np.vdot(b, b)) * b for b in basis)

        w = v - projection

        # Sprawdzamy czy wektor nie jest zerowy (norma > 0)
        norm = np.sqrt(np.vdot(w, w).real)
        if norm > 1e-10:
            # Opcjonalnie: Normalizacja (tworzymy bazę ortonormalną)
            basis.append(w / norm)

    return np.array(basis)


# TEST: Generujemy 2 losowe zespolone wektory dla 1 qubitu (wymiar 2)
dim = 2
complex_random_vectors = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)

# Ortogonalizacja
basis = complex_gram_schmidt(complex_random_vectors)

# Weryfikacja: <u0|u1> powinno być bliskie 0
dot_product = np.vdot(basis[0], basis[1])
print(f"Iloczyn skalarny <u0|u1>: {dot_product:.10f}")

# Weryfikacja normy: <u0|u0> powinno być równe 1
norm_sq = np.vdot(basis[0], basis[0])
print(f"Norma <u0|u0> (powinna być 1): {norm_sq.real:.10f}")
