import jesus_ascends
import sys

argc = len(sys.argv)

if argc == 1:
    print(
        """
        
        Welcome to Mihir Kasmalkar's Acts Project!

        This program contains animations in the terminal for various stories
        in the Book of Acts.

        Here is a list of all of the stories:

            Jesus Ascends

        """
    )

elif argc == 2:

    story = sys.argv[1]

    if story == "Jesus Ascends":
        jesus_ascends.go()

    else:
        print("I can't recognize this story.")
