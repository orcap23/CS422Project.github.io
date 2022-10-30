#This file for uploading solution and compute compare between test set and solution.
#The solution file will be little different between train set.
from math import sqrt
import csv
import os
import datetime


#findnewestfile for find the newest upload file and return file path.
def findnewestfile(uploadfiledir):
    list = os.listdir(uploadfiledir)
    list.sort(key=lambda fn:os.path.getmtime(uploadfiledir + '/' +fn))
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(uploadfiledir+list[-1]))
    filepath = os.path.join(uploadfiledir,list[-1])
    return filepath

filename = os.path.split(findnewestfile("../tsfc/solutions/files/"))[1]
newestfilepath = str(findnewestfile("../tsfc/solutions/files/"))

def testandtrain(newestfilepath):
    with open('./file_upload/train.csv', newline="") as f:
        data_list = []
        reader = csv.reader(f)
        for row in reader:
            data_list.append(row[0])
        new_dat = data_list[0][-4:]
        data_list[0] = new_dat
        test_list = []
        for item in data_list:
            test_list.append(float(item))
        data_list = []

    with open(newestfilepath, newline="") as f:

        reader = csv.reader(f)
        for row in reader:
            data_list.append(row[0])
        new_dat = data_list[0][-4:]
        data_list[0] = new_dat
        train_list = []
        for item in data_list:
            train_list.append(float(item)) # DO NOT FORGET TO GET RID OF - 2 FOR TESTING
        if len(test_list) != len(train_list):
            raise Exception("Train and test list must be same length.")
        return test_list, train_list

"""Mean Average Error"""
def MAE(test, train):
    samp_size = len(test)
    summation = 0

    for i in range(samp_size):
        val = test[i] - train[i]
        summation += abs(val)

    mae = summation / samp_size

    return mae

#print(MAE(test_list, train_list))

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

#print(MAPE(test_list, train_list))

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

#print("RMSE", RMSE(test_list, train_list))

"""Average of a List"""
def AVE(t_list):
    summation = 0
    samp_size = len(t_list)

    for item in t_list:
        summation += item

    return summation / samp_size

"""Correlation Coefficient"""
def COCO(test, train):
    samp_size = len(train)
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

def sortVals(test, train):
    valList = []
    sortList = []
    
    valList.append(["Mean Absolute Error", MAE(test, train)])
    valList.append(["Mean Average Percentage Error", MAPE(test, train)])
    valList.append(["Symmetric Mean Average Percentage Error", SMAPE(test, train)])
    valList.append(["Mean Square Error", MSE(test, train)])
    valList.append(["Root Mean Square Error", RMSE(test, train)])
    valList.append(["Correlation Coefficient", COCO(test, train)])

    for i in range(len(valList)):
        placeholder = valList[0]
        for j in range(len(valList)):
            if valList[j][1] < placeholder[1]:
                placeholder = valList[j]
        placeholder[0] = str(i+1)+ ". " + placeholder[0]
        placeholder[1] = round(placeholder[1], 3)
        placeholder[1] = str(placeholder[1]) + "%"
        sortList.append(placeholder)
        valList.remove(placeholder)

    return sortList

listVals = testandtrain(newestfilepath)
sortedVals = sortVals(listVals[0], listVals[1])
