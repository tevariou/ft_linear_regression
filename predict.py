import model
import csv
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


def main():
    model.train()
    mileage = input("What's your car mileage?\n")
    if is_number(mileage) is False or float(mileage) < 0:
        print('Invalid mileage')
        return
    theta1, theta0 = read_theta()
    x, y, size = model.read_data()
    mileage = (float(mileage) - np.amin(x)) / (np.amax(x) - np.amin(x))
    estimated_price = model.denormalize(theta1 * mileage + theta0, np.amin(y), np.amax(y))
    if estimated_price < 0:
        estimated_price = 0
    print("Estimated price = ", estimated_price)


main()
