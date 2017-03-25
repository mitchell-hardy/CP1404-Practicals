"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
__author__ = 'Mitch Hardy'


STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

# Print(STATE_NAMES).
for key, value in STATE_NAMES.items():
    print("{} is {}".format(key, value))

# Get sate appreviation from user and display full name.
state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

