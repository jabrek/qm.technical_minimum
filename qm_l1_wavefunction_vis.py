# based on https://www.youtube.com/watch?v=iJfw6lDlTuA&list=PL701CD168D02FF56F
# define simple wave function: exp(i*x) + exp(2i*x) for x in [0, 2pi]
# calculate its complex conjugate
# calculate probability density: wave function * complex conjugate
# plot wave function (real and imaginary parts) and probability density
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5 * np.pi, 500)
print(x)

# wave function
psi = np.exp(1j * x) + np.exp(2j * x)
print(psi)
psi_conj = np.conj(psi)
print(psi_conj)

# probability density
prob_density = psi * psi_conj
print(prob_density)
# plot wave function and probability density
plt.plot(x, psi.real, label="Re(ψ)")
plt.plot(x, psi.imag, label="Im(ψ)")
plt.plot(x, prob_density, label="|ψ|^2")
plt.legend()
plt.show()
