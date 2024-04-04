import matplotlib.pyplot as plt

# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [20, 30, 40, 10]
explode = [0, 0.1, 0, 0]

# Create doughnut plot
fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True, colors=plt.cm.tab20.colors)
ax.axis('equal')

# Draw a white circle at the center to create a doughnut plot
centre_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)

# Add a title
plt.title("Doughnut Plot with exploded segment and Shadow effect")

# Show plot
plt.show()
