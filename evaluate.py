import sys


def is_number(s):
    if s is None:
        return False
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():
    mileage = None
    while is_number(mileage) is False:
        mileage = input("What's your car mileage?\n")
    estimated_price = 0.0
    for line in sys.stdin:
        theta_list = line.split()
        if len(theta_list) != 2 or is_number(theta_list[0]) is False or is_number(theta_list[1]) is False:
            print("Estimated price = ", estimated_price)
            continue
        estimated_price = float(mileage) * float(theta_list[1]) + float(theta_list[0])
        print("Estimated price = ", estimated_price)
        break


main()
