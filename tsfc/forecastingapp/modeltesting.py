<<<<<<< HEAD
<<<<<<< HEAD
#This file for uploading solution and compute compare between test set and solution.
#The solution file will be little different between train set.
=======

=======
#This file for uploading solution and compute compare between test set and solution.
#The solution file will be little different between train set.
from math import sqrt
import csv

data_list = []

with open('test.csv', newline="") as f:

    reader = csv.reader(f)
    for row in reader:
        data_list.append(row[0])
    new_dat = data_list[0][-4:]
    data_list[0] = new_dat
    test_list = []
    for item in data_list:
        test_list.append(float(item))
    data_list = []

with open('train.csv', newline="") as f:

    reader = csv.reader(f)
    for row in reader:
        data_list.append(row[0])
    new_dat = data_list[0][-4:]
    data_list[0] = new_dat
    train_list = []
    for item in data_list:
        train_list.append(float(item))

"""Mean Average Error"""
def MAE(test, train):
    samp_size = len(test)
    summation = 0

    for i in range(samp_size):
        val = test[i] - train[i]
        summation += abs(val)

    mae = summation / samp_size

    return mae

# print(MAE(test_list, train_list))

"Mean Average Percentage Error"
def MAPE(test, train):
    samp_size = len(test)
    summation = 0

    for i in range(samp_size):
        if test[i] == 0:
            print("MEAN AVERAGE PERCENTAGE ERROR: CANNOT DIVIDE BY 0")
            return False
        val = (test[i] - train[i]) / test[i]
        summation += abs(val)

    mape = summation / samp_size

    return mape * 100

# print(MAPE(test_list, train_list))

"""Symmetric Mean Average Percentage Error"""
def SMAPE(test, train):
    samp_size = len(test)
    summation = 0
    
    for i in range(samp_size):
        if test[i] + train[i] == 0:
            print("SYMmETRIC MEAN AVERAGE PERCENTAGE ERROR: CANNOT DIVIDE BY 0")
            return False
        val = (abs(train[i] - test[i])) / ((test[i] + train[i]) / 2)
        summation += val

    smape = summation / samp_size

    return smape * 100

# print(SMAPE(test_list, train_list))

"""Mean Square Error"""
def MSE(test, train):
    samp_size = len(test)
    summation = 0

    for i in range(samp_size):
        val = (test[i] - train[i]) ** 2
        summation += val

    mse = summation / samp_size

    return mse

# print(MSE(test_list, train_list))

"""Root Mean Square Error"""
def RMSE(test, train):
    return sqrt(MSE(test, train))

# print(RMSE(test_list, train_list))

"""Average of a List"""
def AVE(t_list):
    summation = 0
    samp_size = len(t_list)

    for item in t_list:
        summation += item

    return summation / samp_size

"""Correlation Coefficient"""
def COCO(test, train):
    samp_size = 5#len(train)
    test_ave = AVE(test)
    train_ave = AVE(train)
    summation_up = 0
    summation_bot_one = 0
    summation_bot_two = 0

    for i in range(samp_size):
        summation_up += (test[i] - test_ave) * (train[i] - train_ave)
        summation_bot_one += (test[i] - test_ave) ** 2
        summation_bot_two += (train[i] - train_ave) ** 2
    
    return (summation_up) / sqrt(summation_bot_one * summation_bot_two)

# print(COCO(train_list, test_list))
