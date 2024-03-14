import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# Generate random data
data = np.random.rand(10, 10)
# Creating a heatmap
sns.heatmap(data)
plt.title('Heatmap Example')
plt.show()
