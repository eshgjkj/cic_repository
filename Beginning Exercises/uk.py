import pandas as pd
import matplotlib.pyplot as pyplot

#read the CSV file and create a dataframe

df = pd.read_csv('scores.csv')

names = df['name']
ages = df['age']
scores = df['score']


mean_score = scores.mean()
median_score = scores.median()
mode_score = scores.mode()
max_score = scores.max()
min_score = scores.min()

print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Most Common Score:", mode_score[0])
print("Highest Score:", max_score)
print("Lowest Score:", min_score)
