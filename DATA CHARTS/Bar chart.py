import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 20, 60]

plt.bar(categories, values)
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
