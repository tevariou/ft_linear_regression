import csv
import matplotlib.pyplot as plt
import math
from os import path


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
    return x, y, size


def normalize(value):
    return [*map(lambda a: (a - min(value)) / (max(value) - min(value)), value)]


def denormalize(theta1, theta0, x, y):
    theta1 = theta1 * (max(y) - min(y)) / (max(x) - min(x))
    theta0 = - theta1 * min(x) + theta0 * (max(y) - min(y)) + min(y)
    return theta1, theta0


def mean_squared_error(theta1, theta0, x, y, m):
    return 1 / m * sum(map(lambda a, b: ((theta1 * a + theta0) - b)**2, x, y))


def plot(theta1, theta0, y, x, m, iteration):
    theta1, theta0 = denormalize(theta1, theta0, x, y)
    # root mean squared error
    rmse = math.sqrt(mean_squared_error(theta1, theta0, x, y, m))
    legend = 'iteration = {} ' \
             'theta1 = {:.2f} ' \
             'theta0 = {:.2f} ' \
             'root mean squared error = {:.2f}'.format(iteration, theta1, theta0, rmse)
    plt.plot([0, 250000], [theta0, theta1 * 250000 + theta0], label=legend)


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
    theta1 = 0
    theta0 = 0
    if not path.exists("data.csv"):
        print("Data is missing")
        write_theta(theta1, theta0)
        return
    x, y, m = read_data()
    mileage = normalize(x)
    price = normalize(y)
    # learning rate
    alpha = 0.1
    iterations = 1000
    for i in range(iterations):
        if i % (iterations / 10) == 0:
            plot(theta1, theta0, y, x, m, i)
        tmp_theta1 = alpha * 1 / m * sum(map(lambda a, b: a * (estimated_price(a, theta1, theta0) - b), mileage, price))
        tmp_theta0 = alpha * 1 / m * sum(map(lambda a, b: estimated_price(a, theta1, theta0) - b, mileage, price))
        theta1 = theta1 - tmp_theta1
        theta0 = theta0 - tmp_theta0
    plt.xlabel('mileage')
    plt.ylabel('price')
    plt.scatter(x, y)
    plt.legend()
    plt.show()
    theta1, theta0 = denormalize(theta1, theta0, x, y)
    write_theta(theta1, theta0)


train()
