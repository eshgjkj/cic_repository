import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('movies.csv')

genre_counts = data['genre'].value_counts()

plt.pie(genre_counts.values, labels = genre_counts.index, autopct = '%1.1f%%')
plt.title('Most Liked Genre')
plt.axis('equal')

plt.show()
