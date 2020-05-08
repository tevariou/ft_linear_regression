import csv
import numpy as np


def read_data():
    y = []
    x = []
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        size = 0
        for row in csv_reader:
            y.append(float(row['price']))
            x.append(float(row['km']))
            size += 1
        csv_file.close()
    return np.array(x), np.array(y), size


def denormalize(value, ref):
    return value * (np.amax(ref) - np.amin(ref)) + np.amin(ref)


def normalize(value):
    return ((value - np.amin(value)) / (np.amax(value) - np.amin(value))).tolist()


def estim(x, theta1, theta0, y):
    return denormalize(theta1 * x + theta0, y)
