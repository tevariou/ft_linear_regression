import csv
from helpers import read_data, estim
from os import path
import numpy as np


def is_number(s):
    if s is None:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_theta():
    with open('theta.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csv_file.close()
            return float(row['theta1']), float(row['theta0'])


def normalize(value, ref):
    return (value - np.amin(ref)) / (np.amax(ref) - np.amin(ref))


def predict():
    if not path.exists("theta.csv"):
        print(f"Please run train.py first")
        return
    if not path.exists("data.csv"):
        print(f"Data is missing")
        return
    mileage = input("What's your car mileage?\n")
    if is_number(mileage) is False or float(mileage) < 0:
        print('Invalid mileage')
        return
    theta1, theta0 = read_theta()
    x, y, size = read_data()
    mileage = float(mileage)
    estimated_price = estim(normalize(float(mileage), x), theta1, theta0, y)
    if estimated_price < 0:
        estimated_price = 0
    print("Estimated price = {:.2f}".format(estimated_price))


predict()
