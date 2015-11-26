from stories import jesus_ascends
from stories import holy_spirit_comes
from stories import peter_heals_lame_beggar
from stories import peter_john_before_sanhedrin
from stories import ananias_and_saphira
from stories import choosing_of_seven
from stories import stephen_siezed
from stories import stephens_speech_to_sanhedrin
from stories import simon_the_sorcerer
from stories import philip_and_ethiopian

import art
import sys

storyList = [jesus_ascends,
             holy_spirit_comes,
             peter_heals_lame_beggar,
             peter_john_before_sanhedrin,
             ananias_and_saphira,
             choosing_of_seven,
             stephen_siezed,
             stephens_speech_to_sanhedrin,
             simon_the_sorcerer,
             philip_and_ethiopian]

# Comment these out during debugging
print()
command = input("story> ").lower()

# DEBUGGING
# .go()
# sys.exit(0)

while command != "":
   
    if command == "help":

        print(
            """
Welcome to Mihir Kasmalkar's Acts Project!

This program contains animations in the terminal for various stories
in the Book of Acts.

Please excuse the bad jokes.

Here is a list of all of the stories:
            """
        )

        for story in storyList:
            print("\t", story.name)

        print()

    else:
        story = [story for story in storyList if story.name == command]
        if len(story) > 0:
            try:
                t = art.Terminal()
                
                t.draw(
                    """
   
        Warning: Some of the text in the following animation
                may be directly from the Bible, but no references
                are provided and it may not be made clear that it
                is a Bible verse
                               
                    """,
                    3
                )

                t.draw(
                    """
   
        Warning: This is so that I do not have to interrupt the
                story with the reference every time a Bible
                verse is quoted
                              
                    """,
                    3
                )

                t.draw(
                    """
   
        Warning: I do not claim the Bible verses to be my
                original work
                    """,
                    3
                )

                story[0].go()
            except SystemExit as se:
                print("Sorry, there was an error: " + str(se))
        else:
            print("I cannot recognize this story")

    command = input("story> ").lower()