import numpy as np
import matplotlib.pyplot as plt


A = np.random.rand(2) + 1j * np.random.rand(2)

inner_product = np.vdot(A, A)

print("Calculating Inner Product ⟨A|A⟩:")
total_check = 0
for i, val in enumerate(A):
    term = np.conj(val) * val
    print(f"Component A[{i}]: {val.real:.4f} + {val.imag:.4f}j")
    print(f"  Term |A[{i}]|² = (conj(A[{i}]) * A[{i}]) = {term.real:.4f} + {term.imag:.4f}j")
    total_check += term

print(f"\nSum of terms: {total_check.real:.4f} + {total_check.imag:.4f}j")
print(f"np.vdot(A, A) result: {inner_product.real:.4f} + {inner_product.imag:.4f}j")
print(f"Is inner product real? {np.isclose(inner_product.imag, 0.0)}")

# Visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot complex vector components
for i, val in enumerate(A):
    ax1.quiver(0, 0, val.real, val.imag, angles='xy', scale_units='xy', scale=1, 
               label=f'A[{i}] = {val.real:.2f} + {val.imag:.2f}j')

ax1.set_title("Vector Components in Complex Plane")
ax1.set_xlabel("Real")
ax1.set_ylabel("Imaginary")
ax1.axhline(0, color='black',linewidth=0.5)
ax1.axvline(0, color='black',linewidth=0.5)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()

# Set limits for ax1
limit = np.max(np.abs(A)) + 0.1
ax1.set_xlim(-limit, limit)
ax1.set_ylim(-limit, limit)

# Plot Inner Product Result
ax2.quiver(0, 0, inner_product.real, inner_product.imag, angles='xy', scale_units='xy', scale=1, 
           color='r', label=f'⟨A|A⟩ = {inner_product.real:.4f} + {inner_product.imag:.4f}j')

ax2.set_title("Inner Product ⟨A|A⟩")
ax2.set_xlabel("Real")
ax2.set_ylabel("Imaginary")
ax2.axhline(0, color='black',linewidth=0.5)
ax2.axvline(0, color='black',linewidth=0.5)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()

# Set limits for ax2
prod_limit = inner_product.real + 0.5
ax2.set_xlim(-0.5, prod_limit)
ax2.set_ylim(-0.5, 0.5)

plt.tight_layout()
plt.show()
