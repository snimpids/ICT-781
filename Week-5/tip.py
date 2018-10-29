def GST(amount, rate = 0.05):
    """ Calculate GST to add to bill. """
    if amount < 0:
        raise ValueError('{} should be non-negative.'.format(amount))
        
    return amount*(1 + rate)

def tip(amount, tip_percent = 0.15):
    """ Calculate the amount with a tip added. """
    
    if amount < 0:
        raise ValueError('{} should be non-negative.'.format(amount))
        
    return amount*(1 + tip_percent)

def main():
    """ Restaurant Bill Calculator. """

    print('Thank you for eating at the Python Cafe.\n')

    # Get the before-tax bill.
    bill = float(input('Please input amount: '))

    tip_rate = -1

    while tip_rate < 0:
        tip_rate = float(input('Please input tip %: '))

    # Adjust if the customer puts in decimal or integer tip percentage.
    if tip_rate % 100 >= 1:
        tip_rate /= 100

    total = GST(bill)
    total = tip(total, tip_rate)

    print('Your total today is ${:.2f}.'.format(total))