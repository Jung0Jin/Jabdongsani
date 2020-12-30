# 데이터 다운로드 
# https://dacon.io/competitions/open/235576/overview/

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터를 불러오자

train = pd.read_csv('train.csv')
train.fillna(train.mean(), inplace=True)

test = pd.read_csv('test.csv')
test.fillna(test.mean(), inplace=True)

print(train.shape)
print(test.shape)

# train_df가 column수가 하나 더 많다. label 인지 확인해보자
print(train.info())
print(test.info())

'''
train 의 count 열을 label로 두고 모델을 학습시킨다.

학습시킨 모델에 validation 을 넣어 예측하며 모델 간 성능을 비교한다.

가장 성능이 좋은 모델에 test를 넣어 예측한다.

'''

# train 의 count 열을 label로 두자
x = train.drop(['count'], axis=1)
y = train['count']

# train 를 train 부분과 validation 부분으로 나누자
from sklearn.model_selection import train_test_split
x_train, x_val, y_train, y_val = train_test_split(x,y,test_size=0.2, random_state=42)

# train 데이터가 8:2로 나뉜 것을 알 수 있다.
print('나뉘기 전 : ', x.shape)
print('나뉜 후 train : ', x_train.shape)
print('나뉜 후 validation : ', x_val.shape)

# 선형회귀 모델로 예측하기

from sklearn.linear_model import LinearRegression

model_reg = LinearRegression()
model_reg.fit(x_train, y_train)

y_val_pred = model_reg.predict(x_val)

# MSE로 평가해보자
from sklearn.metrics import mean_squared_error

MSE_reg = mean_squared_error(y_val, y_val_pred)
print(f'MSE_reg : {MSE_reg}')

# 랜덤포레스트 모델로 예측하기
from sklearn.ensemble import RandomForestRegressor

model_forest = RandomForestRegressor(random_state=42)
model_forest.fit(x_train, y_train)

y_val_pred = model_forest.predict(x_val)

# MSE로 평가해보자
MSE_forest = mean_squared_error(y_val, y_val_pred)
print(f'MSE_forest : {MSE_forest}')

# 어떤 모델이 더 좋을까?
print(f'MSE_reg : {MSE_reg}')
print(f'MSE_forest : {MSE_forest}')

# 랜덤포레스트 회귀가 더 좋아 보인다.
pred = model_forest.predict(test)

# submission 만들기
submission = pd.DataFrame(data=pred, columns=['count'])
submission['id'] = test['id']
submission=submission.set_index('id')
submission.to_csv('my_submission.csv', index=True)
