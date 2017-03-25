__author__ = 'Mitch Hardy'

"""
QuickPick Lottery Generator
"""

def main():
    quantity_quickpicks = int(input("How many quick picks?: "))
    all_quickpicks = []
    quickpick_id = 0
    while quickpick_id < quantity_quickpicks:
        quickpick = quickpick_generator()
        all_quickpicks.append(quickpick)
        quickpick_id += 1
    for quickpick in all_quickpicks:
        print(quickpick)


def quickpick_generator():
    #Randomly generate 6 quickpick numbers into a ticket with error checking.
    import random
    ticket = []
    for i in range (0,6):
        ticket_number = random.randrange(1,46)
        #Error check to see if number already in ticket
        while ticket_number in ticket:
            ticket_number = random.randrange(1, 46)
        else:
            ticket.append(ticket_number)
    ticket.sort()
    return ticket

main()
