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
    print(mileage)


main()
