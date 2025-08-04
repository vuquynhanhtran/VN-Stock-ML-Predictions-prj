import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

#load preprocessed data
train_df = pd.read_csv("train.csv") #don't forget the quotation marks!!!
test_df = pd.read_csv("test.csv")

#define features and target
features = ['Open','High','Low','Volume','Trading_Value'] #X
target = 'Close' #Y

x_train = train_df[features] #practice questions (without answers)
y_train = train_df[target] #the answers to those practice questions
x_test = test_df[features] #new questions you never saw before
y_test = test_df[target] #answers to those new ones (so you can check if you learned)

#train linear regression model
model = LinearRegression()
#teach the model what X leads to Y
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

#evaluate model
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print('Test RSME:', rmse) #Root of mean squared error
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

