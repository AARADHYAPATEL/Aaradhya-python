import textwrap

text = "Horizon, god of war and uncharted are the three best games"

# Wrap the text to a specific width
wrapped_text = textwrap.wrap(text, width=18)

# Print the wrapped text
for line in wrapped_text:
    print(line)
