import csv
import sys
import numpy as np
import matplotlib.pyplot as plt


def normalize_y(y):
    a_min = np.amin(y)
    a_max = np.amax(y)
    return (y - a_min) / (a_max - a_min)


def normalize_x(x):
    a_min = np.amin(x)
    a_max = np.amax(x)
    a_norm = (x - a_min) / (a_max - a_min)
    size, _ = np.shape(a_norm)
    new_x = []
    for i in range(size):
        new_x.append([a_norm[i, 0], 1])
    return np.array(new_x)


def fetch_data():
    y = []
    x = []
    with open('data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        size = 0
        for row in csv_reader:
            if size == 0:
                if len(row) != 2 or row[0] != 'km' or row[1] != 'price':
                    sys.stderr.write("invalid data file\n")
                    return
                size = 1
                continue
            if len(row) != 2:
                continue
            y.append([float(row[1])])
            x.append([float(row[0])])
    return np.array(x), np.array(y)


def main():
    x, y = fetch_data()
    new_x = normalize_x(x)
    alter_x = normalize_y(x)
    new_y = normalize_y(y)
    theta = np.array([[0],
                     [0]])
    alpha = 0.001
    size, _ = np.shape(new_x)
    for i in range(100000):
        if i % 10000 == 0:
            plt.plot([0, 1], [theta[0, 0] * 0 + theta[1, 0], theta[0, 0] * 1 + theta[1, 0]])
        grad = alpha / size * np.dot(new_x.T, np.dot(new_x, theta) - new_y)
        theta = theta - grad
    plt.plot([0, 1], [theta[0, 0] * 0 + theta[1, 0], theta[0, 0] * 1 + theta[1, 0]])
    plt.scatter(alter_x, new_y)
    plt.show()


main()
