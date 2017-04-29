"""CP1404 Prac 07 Exercise - Classes. Person, PersonList Classes"""

__author__ = 'Mitch Hardy'

from Person import Person
from PersonList import PersonList

def person_demo_program():
    """Create a person object and add to PersonList, ending loop when blank entered for name."""

    my_persons = PersonList()
    first_name = input("First Name: ")
    while first_name != "":
        last_name = input("Last Name: ")
        age = input("Age: ")
        new_person = Person(first_name, last_name, age)
        my_persons.add_person(new_person)
        first_name = input("First Name: ")
    PersonList.__str__(my_persons)



person_demo_program()
