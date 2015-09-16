from stories import jesus_ascends
from stories import holy_spirit_comes
import sys

print()
command = input("story> ").lower()

while command != "":
   
    if command == "help":

        print(
            """
        
Welcome to Mihir Kasmalkar's Acts Project!

This program contains animations in the terminal for various stories
in the Book of Acts.

Here is a list of all of the stories:

    Jesus Ascends
            """
        )

    elif command == "jesus ascends":
        jesus_ascends.go()

    elif command == "the holy spirit comes":
        holy_spirit_comes.go()

    else:
        print("I can't recognize this command.")

    command = input("story> ").lower()