import csv
import numpy as np
import matplotlib.pyplot as plt


def normalize_y(y):
    return (y - np.amin(y)) / (np.amax(y) - np.amin(y))


def normalize_x(x):
    size, _ = np.shape(x)
    new_x = []
    for i in range(size):
        new_x.append([(x[i, 0] - np.amin(x)) / (np.amax(x) - np.amin(x)), 1])
    return np.array(new_x)


def read_data():
    y = []
    x = []
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        size = 0
        for row in csv_reader:
            y.append([float(row['price'])])
            x.append([float(row['km'])])
            size += 1
        csv_file.close()
    return np.array(x), np.array(y), size


def denormalize(value, a_min, a_max):
    return value * (a_max - a_min) + a_min


def f(x, theta1, theta0, y):
    return denormalize(theta1 * x + theta0, np.amin(y), np.amax(y))


def plot(theta, y, iteration, mse):
    legend = f'iter = {iteration} theta1 = {"{0:.4f}".format(theta[0, 0])} theta0 = {"{0:.4f}".format(theta[1, 0])} error: {"{0:.4f}".format(mse)}'
    plt.plot([0, 250000], [f(0, theta[0, 0], theta[1, 0], y), f(1, theta[0, 0], theta[1, 0], y)], label=legend)


def write_data(theta):
    with open("theta.csv", 'w') as csv_file:
        fieldnames = ['theta1', 'theta0']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'theta1': f'{theta[0, 0]}', 'theta0': f'{theta[1, 0]}'})
        csv_file.close()


def train():
    x, y, size = read_data()
    theta = np.array([[0],
                     [0]])
    alpha = 0.1
    iterations = 2500
    for i in range(iterations):
        if i % (iterations / 10) == 0:
            mse = 1 / (2 * size) * np.sum((np.dot(normalize_x(x), theta) - normalize_y(y))**2)
            plot(theta, y, i, mse)
        theta = theta - alpha / size * np.dot(normalize_x(x).T, np.dot(normalize_x(x), theta) - normalize_y(y))
    plt.xlabel('km')
    plt.ylabel('price')
    plt.scatter(x, y)
    plt.legend()
    plt.show()
    write_data(theta)
