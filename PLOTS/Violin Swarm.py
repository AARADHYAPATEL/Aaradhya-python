import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# Generate random data
data = np.random.randn(100)
# Create a violin swarm plot
sns.violinplot(data=data, inner=None, color='lightgray')
sns.swarmplot(data=data, color='blue', alpha=0.5)
plt.title('Violin Swarm Plot Example')
plt.show()
