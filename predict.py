import csv
from os import path


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


def predict():

    mileage = input("What's your car mileage?\n")
    if is_number(mileage) is False or float(mileage) < 0:
        print('Invalid mileage')
        return
    theta1, theta0 = 0, 0
    if path.exists("theta.csv"):
        theta1, theta0 = read_theta()
    estimated_price = float(mileage) * theta1 + theta0
    if estimated_price < 0:
        estimated_price = 0
    print("Estimated price = {:.2f}".format(estimated_price))


predict()
