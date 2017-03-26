"""
Create a dictionary containing names and relative DOB from user input.
Display age of name from user query.
"""
__author__ = 'Mitch Hardy'


def lists_to_dictionary():
    """Determine database size, get names and DOBs from user,
       use dict function to compile dictionary from lists and display age of user name query."""
    DATABASE_SIZE = get_db_size()
    dobs, names = get_names_dobs(DATABASE_SIZE)
    names_dobs_dict = dict(zip(names, dobs))
    age_of_person(names_dobs_dict)


def get_db_size():
        db_size = 0
        correct_db_size = False
        while not correct_db_size:
            try:
                db_size = int(input("Please advise how many people will be added: "))
                correct_db_size = True
            except ValueError:
                print("Incorrect input, please enter numbers only!")
        return db_size


def get_names_dobs(size):
    """Create 2 lists of names and DOB's from user input relative to inputted database size.
    Error check for correct date format. """
    import _datetime
    names = []
    dobs = []
    for i in range(0, size):
        name = input("Please enter the name for person {}:".format(i + 1)).lower()
        names.append(name)
        dob = ""
        correct_dob = False
        while not correct_dob:
            try:
                dob = input("Please enter the DOB for person {}:".format(i + 1))
                correct_dob = _datetime.datetime.strptime(dob, "%d/%m/%Y")

            except ValueError:
                print("Incorrect DOB format, please enter as DD/MM/YYYY!")
        dobs.append(dob)
    return dobs, names


def age_of_person(names_dobs_dict):
    """Ask user to enter a name, if name in Dictionary, calculate and display age use datetime functions.
    If name not in dictionary, display name data to user."""
    import _datetime
    age_query = input("Please enter a name to see their age: ").lower()
    while age_query not in names_dobs_dict:
        print("We have no data for that person, please choose from these people: ")
        for key in names_dobs_dict:
            print(str(key).capitalize())
        age_query = input("Please enter a name to see their age: ").lower()
    if age_query in names_dobs_dict:
        today_date = _datetime.date.today()
        current_year = int(today_date.strftime("%Y"))
        # TODO FIX THIS -----  person_born = int(names_dobs_dict(age_query[6:]))
        persons_age = current_year - person_born
        print("{} is {} years old.".format(age_query, persons_age).capitalize())


lists_to_dictionary()
