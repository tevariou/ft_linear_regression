import csv
import sys
import numpy as np
import matplotlib.pyplot as plt


def a_min_max(array):
    return np.amin(array), np.amax(array)


def normalize_y(y):
    a_min, a_max = a_min_max(y)
    return (y - a_min) / (a_max - a_min)


def normalize_x(x):
    a_min, a_max = a_min_max(x)
    size, _ = np.shape(x)
    new_x = []
    for i in range(size):
        new_x.append([(x[i, 0] - a_min) / (a_max - a_min), 1])
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
                size += 1
                continue
            if len(row) != 2:
                continue
            y.append([float(row[1])])
            x.append([float(row[0])])
            size += 1
    return np.array(x), np.array(y), size


def denormalize(value, a_min, a_max):
    return value * (a_max - a_min) + a_min


def plot(theta, x, y, iteration):
    plt.plot([0, denormalize(1, *a_min_max(x))],
             [denormalize(theta[0, 0] * 0 + theta[1, 0], *a_min_max(y)), denormalize(theta[0, 0] * 1 + theta[1, 0], *a_min_max(y))],
             label=f'iter = {iteration} theta1 = {"{0:.4f}".format(theta[0, 0])} theta0 = {"{0:.4f}".format(theta[1, 0])}')


def main():
    x, y, size = fetch_data()
    theta = np.array([[0],
                     [0]])
    alpha = 0.01
    iterations = 10000
    for i in range(iterations):
        theta = theta - alpha / size * np.dot(normalize_x(x).T, np.dot(normalize_x(x), theta) - normalize_y(y))
        if (i + 1) % 1000 == 0:
            plot(theta, x, y, i)
    plt.xlabel('km')
    plt.ylabel('price')
    plt.scatter(x, y)
    plt.legend()
    plt.show()


main()
