

__author__ = 'Mitch Hardy'


def lists_to_dictionary():
    names = []
    dobs = []
    import _datetime




    for i in range(0, 1):
        name = input("Please enter the name for person {}:".format(i+1).lower())
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



        #         correct_dob = _datetime.date.strftime(check_dob, "%d/%m/%Y")
        #     except ValueError:
        #         p
        # dobs.append(dob)



    #
    # print(names)
    # print(dobs)

    # names_dobs_dict = dict(zip(names, dobs))
    #
    # age_query = input("Please enter a name to see their age: ").lower
    # while age_query not in names_dobs_dict:
    #     print("We have no data for that person, please choose from these persons: ")
    #     for key in names_dobs_dict:
    #         print(key, end="\n")
    #     age_query = input("Please enter a name to see their age: ").lower
    #
    # if age_query in names_dobs_dict:
    #     for key, value in names_dobs_dict.items():
    #         print("{} was born on {}".format(key, value))

lists_to_dictionary()
