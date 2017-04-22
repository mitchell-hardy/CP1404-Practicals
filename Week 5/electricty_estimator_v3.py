"""
Electricity Estimator Exercise - Upgrade to dictionary usage.
"""

__author__ = 'Mitch Hardy'


def electricity_estimator():
    """
    Use dictionary to store Constant data and calculate electricity costs as per user input.
    """
    TARIFF_DICT = {'11': 0.244618, '31': 0.136928, '10': 0.444618,
                   '66': 0.555428, '15': 0.34318, '00': 0.56789}
    price_kwh = get_tariff(TARIFF_DICT)
    daily_kwh = get_daily_kwh()
    billings_days = get_billing_days()
    bill_estimation = calculate_bill(price_kwh, daily_kwh, billings_days)
    print("Estimated Bill: ${:.2f}".format(bill_estimation))


def get_tariff(TARIFF_DICT):
    """
    Return the user selected tariff.
    """
    for key in TARIFF_DICT:
        print("- " + key)
    user_tariff = input("Please choose which tariff in use from the above: ")
    while user_tariff not in TARIFF_DICT:
        print("Incorrect value, please enter from the provided tariffs only!")
        for key in TARIFF_DICT:
            print("-" + key)
        user_tariff = input("Please choose which tariff in use from the above: ")
    return TARIFF_DICT[user_tariff]


def get_daily_kwh():
    """
    Return daily kwh usage.
    """
    daily_kwh = float(input("Please enter the amount of KWH used daily:  "))
    while daily_kwh < 0:
        print("Incorrect value, please enter numbers greater than 0 only - e.g. 4.52")
        daily_kwh = float(input("Please enter the amount of KWH used daily:  "))
    return daily_kwh


def get_billing_days():
    """
    Return quantity of billing days.
    """
    billing_days = int(input("Please enter the amount of billings days: "))
    while billing_days < 0:
        print("Incorrect value, please enter numbers greater than 0 only - e.g. 60")
        billing_days = int(input("Please enter the amount of billings days: "))
    return billing_days

def calculate_bill(price_kwh, daily_kwh, billings_days):
    """
    Calculate and return estaimated electricty costs.
    """
    bill_estimation = (billings_days * daily_kwh * price_kwh)
    return bill_estimation

electricity_estimator()
