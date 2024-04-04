import plotly.graph_objects as go

# Sample data
labels = ['A', 'B', 'C', 'D']
values = [20, 30, 40, 10]

# Create doughnut plot
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.5)])
fig.update_layout(title_text="Doughnut Plot")

# Show plot
fig.show()
