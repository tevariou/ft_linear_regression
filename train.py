import csv
import matplotlib.pyplot as plt
from helpers import read_data, denormalize, estim
import math
import numpy as np
from os import path


def normalize(value):
    return ((value - np.amin(value)) / (np.amax(value) - np.amin(value))).tolist()


def plot(theta1, theta0, y, iteration, rmse):
    legend = 'iteration = {} ' \
             'theta1 = {:.2f} ' \
             'theta0 = {:.2f} ' \
             'root mean squared error = {:.2f}'.format(iteration, theta1, theta0, rmse)
    plt.plot([0, 250000], [estim(0, theta1, theta0, y), estim(1, theta1, theta0, y)], label=legend)


def write_theta(theta1, theta0):
    with open("theta.csv", 'w') as csv_file:
        fieldnames = ['theta1', 'theta0']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'theta1': f'{theta1}', 'theta0': f'{theta0}'})
        csv_file.close()


def estimated_price(km, theta1, theta0):
    return theta1 * km + theta0


def train():
    if not path.exists("data.csv"):
        print(f"Data is missing")
        return
    x, y, m = read_data()
    km = normalize(x)
    price = normalize(y)
    # learning rate
    alpha = 0.1
    iterations = 1000
    theta1 = 0
    theta0 = 0
    for i in range(iterations):
        if i % (iterations / 10) == 0:
            # mean squared error
            mse = 1 / m * sum(map(lambda a, b: (denormalize(theta1 * a + theta0, y) - denormalize(b, y))**2, km, price))
            # root mean squared error
            rmse = math.sqrt(mse)
            plot(theta1, theta0, y, i, rmse)
        tmp_theta1 = alpha * 1 / m * sum(map(lambda a, b: a * (estimated_price(a, theta1, theta0) - b), km, price))
        tmp_theta0 = alpha * 1 / m * sum(map(lambda a, b: estimated_price(a, tmp_theta1, tmp_theta0) - b, km, price))
        theta1 = theta1 - tmp_theta1
        theta0 = theta0 - tmp_theta0
    plt.xlabel('km')
    plt.ylabel('price')
    plt.scatter(x, y)
    plt.legend()
    plt.show()
    write_theta(theta1, theta0)


train()
