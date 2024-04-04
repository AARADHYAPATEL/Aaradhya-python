import matplotlib.pyplot as plt

# Sample data
labels = ['Category A', 'Category B', 'Category C', 'Category D']  # Added an extra label
sizes = [20, 30, 40, 10]

# Create doughnut plot
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Draw a white circle at the center to create a doughnut plot
centre_circle = plt.Circle((0, 0), 0.7, color='white', fc='white', linewidth=1.25)
fig.gca().add_artist(centre_circle)

# Add a title
plt.title('Doughnut Plot')

# Show plot
plt.show()
