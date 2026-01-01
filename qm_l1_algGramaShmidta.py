import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def norm(v):
    norm = np.linalg.norm(v)
    return norm


def norm2(v):
    norm = np.sqrt(np.vdot(v, v).real)
    return norm


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - sum((np.vdot(b, v) / np.vdot(b, b)) * b for b in basis)
        w_norm = norm2(w)
        if w_norm.real > 1e-10:
            basis.append(w / w_norm)  # normalize
    return np.array(basis)


dim = 3

# Create 4 random vectors in 4 dimensions (our starting basis)
# random_vectors = np.random.rand(dim, dim)

# create 4 random complex vectors in 4 dimensions (our starting basis)
random_vectors = np.random.randn(dim, dim) + 1j * np.random.randn(dim, dim)

# ortonalize them using Gram-Schmidt process
orhtogonal_basis = gram_schmidt(random_vectors)

print(f"Number of perpendicular vectors found: {len(orhtogonal_basis)}")

# Verify orthogonality
for i in range(len(orhtogonal_basis)):
    for j in range(i + 1, len(orhtogonal_basis)):
        ip = np.vdot(orhtogonal_basis[i], orhtogonal_basis[j])
        print(f"Inner product <u{i}|u{j}>: {ip:.10f}")

# visualize the vectors using matplotlib
fig = plt.figure()  # create a figure
ax = fig.add_subplot(111, projection="3d")  # add a 3D subplot
# https://matplotlib.org/stable/gallery/color/named_colors.html
colors_orto = ["r", "g", "b"]
colors_rand = ["lightcoral", "lightgreen", "lightblue"]
for i, vec in enumerate(orhtogonal_basis):
    ax.quiver(
        0,
        0,
        0,
        vec[0].real,
        vec[1].real,
        vec[2].real,
        color=colors_orto[i],
        label=f"u{i}",
    )
    ax.text(
        orhtogonal_basis[i][0].real,
        orhtogonal_basis[i][1].real,
        orhtogonal_basis[i][2].real,
        f"u{i}: {norm2(orhtogonal_basis[i]).real:.2f}",
    )
for i, vec in enumerate(random_vectors):
    ax.quiver(
        0,
        0,
        0,
        vec[0].real,
        vec[1].real,
        vec[2].real,
        color=colors_rand[i],
        label=f"v{i}",
    )
    ax.text(
        random_vectors[i][0].real,
        random_vectors[i][1].real,
        random_vectors[i][2].real,
        f"v{i}: {norm2(random_vectors[i]).real:.2f}",
    )

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
# add labelsto vectors

# ax.text(
#     orhtogonal_basis[1][0].real,
#     orhtogonal_basis[1][1].real,
#     orhtogonal_basis[1][2].real,
#     f"u1",
# )
# ax.text(
#     orhtogonal_basis[2][0].real,
#     orhtogonal_basis[2][1].real,
#     orhtogonal_basis[2][2].real,
#     f"u2",
# )

ax.legend()
plt.show()
