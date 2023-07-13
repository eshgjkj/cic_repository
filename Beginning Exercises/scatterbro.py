import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scores.csv')

names = df['name']
scores = df['score']

plt.scatter(names, scores)

plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores by Name')
plt.xticks(rotation=70)
plt.show()
