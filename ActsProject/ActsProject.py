from stories import jesus_ascends
from stories import holy_spirit_comes
import sys

storyList = [jesus_ascends, holy_spirit_comes]


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

    else:
        story = [story for story in storyList if story.name == command]
        if story[0] != None:
            story[0].go()
        else:
            print("I cannot recognize this story")

    command = input("story> ").lower()