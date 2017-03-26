

__author__ = 'Mitch Hardy'


def lists_to_dictionary():
    names = []
    dobs = []
    import _datetime

    for i in range(0, 1):
        name = input("Please enter the name for person {}:".format(i+1)).lower()
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

    names_dobs_dict = dict(zip(names, dobs))

    age_query = input("Please enter a name to see their age: ").lower()
    while age_query not in names_dobs_dict:
        print("We have no data for that person, please choose from these people: ")
        for key in names_dobs_dict:
            print(key, end="\n")
        age_query = input("Please enter a name to see their age: ").lower()



    if age_query in names_dobs_dict:
        for key, value in names_dobs_dict.items():
            todays_date = _datetime.date.today()
            current_year = int(todays_date.strftime("%Y"))
            person_born = int(value[6:])
            persons_age = current_year - person_born
            print("{} is {} years old.".format(key, persons_age).capitalize())

            # print("{} was born on {}".format(persons_age))

lists_to_dictionary()
