
"""CP1404 Prac 07 Intermediate Exercise - Programming Languages"""

__author__ = 'Mitch Hardy'


class ProgrammingLanguage:

    def __init__(self, name='', typing='', reflection=False, year=0):
        """Initialise a programming language instance
        name: name of programming language
        typing: static or dynamic supported
        reflection: is the ability for a program to determine various
        pieces of information about an object at run-time.
        year: year released"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year


    def __str__(self):
        """defined string print to format required."""
        print("{}, {} Typing, Reflection={}, First appeared in {}"
              .format(self.name, self.typing, self.reflection, self.year))

    def print_if_dynamic(self):
        if self.typing == "Dynamic":
            print(self.name)
