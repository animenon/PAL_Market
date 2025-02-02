import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
import pandas_datareader.data as web

#style.use('ggplot')
#%matplotlib inline
end=dt.datetime.now()
start = dt.datetime(end.year-1,end.month,end.day)
df = web.DataReader('TSLA','yahoo',start,end)
df.to_csv('TSLA.csv')
df = pd.read_csv('TSLA.csv')
# looking at the first five rows of the data
print(df.head())
print('\n Shape of the data:')
print(df.shape)

# setting the index as date
df['Date'] = pd.to_datetime(df.Date,format='%Y-%m-%d')
df.index = df['Date']

#creating dataframe with date and the target variable
data = df.sort_index(ascending=True, axis=0)
new_data = pd.DataFrame(index=range(0,len(df)),columns=['Date', 'Close'])

for i in range(0,len(data)):
     new_data['Date'][i] = data['Date'][i]
     new_data['Close'][i] = data['Close'][i]

# NOTE: While splitting the data into train and validation set, we cannot use random splitting since that will destroy the time component. So here we have set the last year’s data into validation and the 4 years’ data before that into train set.

raw_size = int(df.shape[0]*0.75)
print(df.size, raw_size)
# splitting into train and validation
train = new_data[:raw_size]
valid = new_data[raw_size:]

# shapes of training set
print('\n Shape of training set:')
print(train.shape)

# shapes of validation set
print('\n Shape of validation set:')
print(valid.shape)

# In the next step, we will create predictions for the validation set and check the RMSE using the actual values.
# making predictions

preds = []
for i in range(0,valid.shape[0]):
    a = train['Close'][len(train)-248+i:].sum() + sum(preds)
    b = a/248
    preds.append(b)

# checking the results (RMSE value)
#rms=np.sqrt(np.mean(np.power((np.array(valid['Close'])-preds),2)))
#print('\n RMSE value on validation set:')
#print(rms)
for i in range(len(preds)):
  print(np.array(valid['Close'])[i], preds[i])

