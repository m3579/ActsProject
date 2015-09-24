from stories import jesus_ascends
from stories import holy_spirit_comes
from stories import peter_heals_lame_beggar
from stories import peter_john_before_sanhedrin
import sys

storyList = [jesus_ascends, holy_spirit_comes, peter_heals_lame_beggar, peter_john_before_sanhedrin]

print()
command = input("story> ").lower()

# DEBUGGING
# <story>.go()
# sys.exit(0)

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
        if len(story) > 0:
            story[0].go()
        else:
            print("I cannot recognize this story")

    command = input("story> ").lower()