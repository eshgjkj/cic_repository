import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('Netflix_Revenue.csv')

dates = pd.to_datetime(df['Date'], dayfirst = True)

uacn_revenue = df['UACN Revenue']
model = LinearRegression()

X = dates.astype('int64').values.reshape(-1, 1)

model.fit(X, uacn_revenue)

predicted_revenue = model.predict(X)

mse = mean_squared_error(uacn_revenue, predicted_revenue)
rmse = mse **0.5

print("Root Mean Squared Error:", rmse)

plt.plot(dates, uacn_revenue, label = 'Actual Revenue')
plt.plot(dates, predicted_revenue, label = 'Predicted Revenue')

plt.xlabel('Data')
plt.ylabel('Revenue')
plt.title('Actual vs Predicted UACN Revenue Over Time')
plt.legend()

plt.xticks(rotation = 45)

plt.show()
