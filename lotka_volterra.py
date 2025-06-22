# lotka_volterra.py

# %%
# Top-Down Predator-Prey Model
# Interactive Lotka-Volterra equations with sliders.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from ipywidgets import interact, FloatSlider

# %%
def lotka_volterra(state, t, alpha, beta, delta, gamma):
    x, y = state
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# %%
def simulate_lotka_volterra(alpha=1.0, beta=0.1, delta=0.075, gamma=1.5):
    t = np.linspace(0, 50, 1000)
    init = [10, 5]
    sol = odeint(lotka_volterra, init, t, args=(alpha, beta, delta, gamma))
    x, y = sol[:, 0], sol[:, 1]

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(t, x, label="Prey", color="green")
    plt.plot(t, y, label="Predator", color="red")
    plt.title("Predator-Prey Over Time")
    plt.xlabel("Time"); plt.ylabel("Population"); plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x, y, color="purple")
    plt.title("Phase Space")
    plt.xlabel("Prey"); plt.ylabel("Predator")
    plt.tight_layout()
    plt.show()

# %%
interact(simulate_lotka_volterra,
         alpha=FloatSlider(1.0, 0.1, 2.0, 0.1),
         beta=FloatSlider(0.1, 0.01, 0.3, 0.01),
         delta=FloatSlider(0.075, 0.01, 0.2, 0.005),
         gamma=FloatSlider(1.5, 0.1, 3.0, 0.1))
