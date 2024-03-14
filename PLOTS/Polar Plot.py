import matplotlib.pyplot as plt
import numpy as np

# Sample data
theta = np.linspace(0, 2*np.pi, 100)
r = np.sin(3*theta)

# Create a polar plot
plt.polar(theta, r)
plt.title('Polar Plot Example')
plt.show()
