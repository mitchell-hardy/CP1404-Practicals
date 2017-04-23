"""CP1404 Prac 07 Intermediate Exercise - Programming Languages - run program"""

__author__ = 'Mitch Hardy'

from ProgrammingLanguage import ProgrammingLanguage


def main():

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    languages_list = [ruby, python, vb]
    for language in languages_list:
        ProgrammingLanguage.__str__(language)
    print("The dynamically typed languages are:")
    for language in languages_list: # Print name of language if typing is dynamic.
        ProgrammingLanguage.print_if_dynamic(language)












main()
