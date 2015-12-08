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
from stories import sauls_conversion
from stories import aeneus_and_dorcas
from stories import peters_vision
from stories import peters_miraculous_escape

from art import Terminal
import sys

storyList = [jesus_ascends,                 # 1
             holy_spirit_comes,             # 2
             peter_heals_lame_beggar,       # 3
             peter_john_before_sanhedrin,   # 4
             ananias_and_saphira,           # 5
             choosing_of_seven,             # 6
             stephen_siezed,                # 7
             stephens_speech_to_sanhedrin,  # 8
             simon_the_sorcerer,            # 9
             philip_and_ethiopian,          # 10
             sauls_conversion,              # 11
             aeneus_and_dorcas,             # 12
             peters_vision,                 # 13
             peters_miraculous_escape       # 14   
            ]

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
            t = Terminal()
            t.draw(
        """




       
        The verses in this animation were taken from
        """ + story[0].reference + """





        """,
        3
    )
            t.draw(
        r"""


     
           /\                              
          /  \                            o   o        
         /    \        $$$$     ------    
        /      \       $        |         o   o
       /        \      $$$$     |         o   o
      /          \        $     |         o   o
     /            \    $$$$     ------    o   o


        """,
        0.6
    )
            t.draw(
        r"""


     
           /\                              
          /  \                      !       
         /    \        ------    =======     $$$$
        /      \       |            !        $
       /        \      |            !        $$$$
      /          \     |            !           $
     /            \    ------       !        $$$$


        """,
        0.6
    )
            t.draw(
        r"""


     
                                   
            
     
     
     
     
     


        """,
        1
    )

            story[0].go(t)
        else:
            print("I cannot recognize this story")

    command = input("story> ").lower()