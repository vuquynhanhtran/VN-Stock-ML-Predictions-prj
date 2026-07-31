import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

train_df = pd.read_csv("train.csv") 
test_df = pd.read_csv("test.csv")

features = ['Open','High','Low','Volume','Trading_Value'] #X
target = 'Close' 

x_train = train_df[features] 
y_train = train_df[target] 
x_test = test_df[features] 
y_test = test_df[target] 


model = LinearRegression()

model.fit(x_train,y_train)
y_pred = model.predict(x_test)


rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print('Test RSME:', rmse) #Root of mean squared error
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

