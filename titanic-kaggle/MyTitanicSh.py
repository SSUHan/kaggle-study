
# coding: utf-8

# In[228]:

import pandas as pd
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')
train.info()


# In[229]:

cols = ['Name', 'Ticket', 'Cabin']
train = train.drop(cols, axis=1)
train.info()


# In[230]:

train = train.dropna()
train.info()


# In[231]:

def pandas_drop_columns(pandas_object):
    cols = ['Name', 'Ticket', 'Cabin']
    pandas_object = pandas_object.drop(cols, axis=1)
    pandas_object = pandas_object.dropna()
    return pandas_object

def pandas_convert_columns(pandas_object):
    dummies = []
    cols = ['Pclass', 'Sex', 'Embarked']
    for col in cols:
        dummies.append(pd.get_dummies(pandas_object[col]))
    temp_dummies = pd.concat(dummies, axis=1)
    pandas_object = pd.concat((pandas_object, temp_dummies), axis=1)
    pandas_object = pandas_object.drop(['Pclass', 'Sex', 'Embarked'], axis=1)
    return pandas_object


# In[232]:

pandas_convert_columns(train).info()


# In[233]:

dummies = []
cols = ['Pclass','Sex','Embarked']
for col in cols:
    print(pd.get_dummies(train[col]))
    dummies.append(pd.get_dummies(train[col]))


# In[234]:

titanic_dummies = pd.concat(dummies,axis=1)
titanic_dummies.info()


# In[235]:

train = pd.concat((train, titanic_dummies), axis=1)
train.info()


# In[236]:

train = train.drop(['Pclass', 'Sex', 'Embarked'], axis=1)
train.info()


# In[237]:

train.interpolate()
train.info()


# In[238]:

#test['Survived'] = test['Sex'].map({'female':1, 'male':0}).astype(int)
# test['Survived'] = 0
# for index, row in test.iterrows():
#     if row['Sex'] == 'female':
#         test['Survived'][index] = 1
#     else:
#         # male
#         if row['Pclass'] == 1:
#             test['Survived'][index] = 1
#         else:
#             test['Survived'][index] = 0

from sklearn import cross_validation
import numpy as np
y = train['Survived'].values
X = train.values
X = np.delete(X,1,axis=1)


# In[239]:

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=1)
type(X_train)


# In[240]:

from sklearn import tree
dt = tree.DecisionTreeClassifier(max_depth=6)
dt.fit(X_train, y_train)
dt.score(X_test, y_test)


# In[241]:

test = pd.read_csv('test.csv')
test = pandas_drop_columns(test)
X_result_pandas = pandas_convert_columns(test)
print(X_result_pandas.info())
print(type(X_result_pandas))
print(type(X_result_pandas.values))
y_result = dt.predict(X_result_pandas.values)
print(type(y_result))


# In[242]:

X_result_np = X_result_pandas.values
# print(X_result_np)
output = np.column_stack((X_result_np[:,0], y_result))
submission_format = pd.DataFrame(output.astype('int'), columns=['PassengerID', 'Survived'])
submission_format.info()


# In[243]:

submission_format.to_csv('discisoin_tree_depth6.csv', index=False)

