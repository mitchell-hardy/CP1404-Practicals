__author__ = 'Mitch Hardy'

def main():
    TARIFF_11 = 0.244618
    TARIFF_31 = 0.136928
    price_kwh = get_tariff(TARIFF_11,TARIFF_31)
    daily_kwh = get_daily_kwh()
    billings_days = get_billing_days()
    bill_estimation = calculate_bill(price_kwh, daily_kwh, billings_days)
    print("Estimated Bill: ${:.2f}".format(bill_estimation))

def get_tariff(TARIFF_11, TARIFF_31):

    tariff = int(input("Please choose which tariff in use, 11 or 31: "))
    while tariff not in (11, 31):
        print("Incorrect value, please enter 11 or 31!")
        tariff = int(input("Please choose which tariff in use, 11 or 31: "))

    if tariff == 11:
        tariff = TARIFF_11

    elif tariff == 31:
        tariff = TARIFF_31

    return tariff


def get_daily_kwh():

    daily_kwh = float(input("Please enter the amount of KWH used daily:  "))
    while daily_kwh < 0:
        print("Incorrect value, please enter numbers greater than 0 only - e.g. 4.52")
    else:
        return daily_kwh


def get_billing_days():

    billing_days = int(input("Please enter the amount of billings days: "))
    while billing_days < 0:
        print("Incorrect value, please enter numbers greater than 0 only - e.g. 60")
    else:
        return billing_days

def calculate_bill(price_kwh, daily_kwh, billings_days):

    bill_estimation = (billings_days * daily_kwh * price_kwh)
    return bill_estimation

main()





