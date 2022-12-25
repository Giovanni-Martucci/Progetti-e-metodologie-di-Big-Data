import warnings
warnings.filterwarnings("ignore")
from sklearn.datasets import load_boston
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from sklearn.linear_model import SGDRegressor
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
from numpy import random
from sklearn.model_selection import train_test_split


def SGD(train_data, learning_rate, n_iter, k):
    # Initially we will keep our W and B as 0 as per the Training Data
    w = np.zeros(shape=(train_data.shape[0], train_data.shape[1] ))
    b = 0
    cur_iter = 1

    while cur_iter <= n_iter:

        # We will create a small training data set of size K
        temp = train_data.sample(k)
        y = np.array(temp)

        w_gradient = np.zeros(shape=(1, train_data.shape[1] - 1))
        b_gradient = 0

        for i in range(k):  # Calculating gradients for point in our K sized dataset
            for j in range(train_data.shape[1]):
                prediction = np.dot(w[i], y[i]) + b # 
                w_gradient = w_gradient + (-2) * w[i][j] * (y[i][j] - prediction) #qui scrivere la derivata dell'errore RMSE 
                b_gradient = b_gradient + (-2) * (y[i] - prediction) #qui scrivere la derivata dell'errore RMSE 

        # Updating the weights(W) and Bias(b) with the above calculated Gradients
        w = w - learning_rate * (w_gradient / k)
        b = b - learning_rate * (b_gradient / k)
        # Incrementing the iteration value
        cur_iter = cur_iter + 1

    return w, b, losses

def predict(x, w, b):
    y_pred = []
    for i in range(len(x)):
        y = np.asscalar(np.dot(w, x[i]) + b)
        y_pred.append(y)
    return np.array(y_pred)








enzyme_data = pd.read_csv('enzyme.txt', delimiter="\t")
data = np.arange(1000)
# enzyme_data['output'] = np.random.choice(data, 664)
enzyme_data = enzyme_data.iloc[:, 1:]
X_enz = enzyme_data.to_numpy()
Y_enz = enzyme_data.to_numpy()
#X_enz = enzyme_data.drop('output', axis=1).to_numpy()
#X_enz = np.zeros(445)
'''for cel in range(663):
    arr = np.zeros(445)
    arr[:4] = 1
    np.random.shuffle(arr)
    arr = arr.astype(int)
    X_enz = np.vstack((X_enz, arr)).astype(int)'''
#x_train, x_test, y_train, y_test = train_test_split(X_enz, Y_enz, test_size=0.3)



#print("X Shape: ", X_enz.shape)
#print("Y Shape: ", Y_enz.shape)
'''print("X_Train Shape: ", x_train.shape)
print("X_Test Shape: ", x_test.shape)
print("Y_Train Shape: ", y_train.shape)
print("Y_Test Shape: ", y_test.shape)'''

'''# standardizing data
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
'''
# Adding the PRIZE Column in the data
train_data = pd.DataFrame(x_train)
'''for i in range(train_data.shape[0]):
    train_data.loc[i, 'output'] = str(y_train[i])

train_data.head(3)'''

'''x_test = np.array(x_test)
y_test = np.array(y_test)
'''
# SkLearn SGD classifier
'''n_iter = 1000
clf_ = SGDRegressor(max_iter=n_iter)
clf_.fit(x_train, y_train)
y_pred_sksgd = clf_.predict(x_test)
print('Mean Squared Error :', mean_squared_error(y_test, y_pred_sksgd))'''


# Manual SGD
w, b, losses = SGD(train_data, 0.01, 1000, 100)
y_pred_customsgd_improved = predict(x_test, w, b)

plt.scatter(y_test, y_pred_customsgd_improved)
plt.grid()
plt.xlabel('Actual y')
plt.ylabel('Predicted y')
plt.title('Scatter plot from actual y and predicted y')
plt.show()
print('Mean Squared Error :', mean_squared_error(y_test, y_pred_customsgd_improved))