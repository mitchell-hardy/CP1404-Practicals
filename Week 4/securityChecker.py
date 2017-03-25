__author__ = 'Mitch Hardy'

"""
Check username input from user against list of known names and Permit or Deny access by print statement
"""


def main():
#Define permitted usernames and check inputted username from user.
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_name = get_user_name()
    valid_user = usernames_check(user_name,usernames)
    if valid_user:
        print("Access Granted")
    else:
        print("Access Denied")


def get_user_name():
# Get username from user
    name = input("Please enter your user name: ")
    return name


def usernames_check(user_name, usernames):
# Check if user name in list of permitted names.
    if user_name in usernames:
        return True
    else:
        return False

main()
