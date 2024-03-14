import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Create an area plot
plt.fill_between(x, y1, color="skyblue", alpha=0.4)
plt.fill_between(x, y2, color="salmon", alpha=0.4)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Area Plot Example')
plt.show()