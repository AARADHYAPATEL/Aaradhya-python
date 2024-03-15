from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read text from a file
with open('key.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Generate word cloud
wordcloud = WordCloud(width=1100, height=550, background_color='white').generate(text)

# Display the generated wordcloud using matplotlib
plt.figure(figsize=(13, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
