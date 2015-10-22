from art import Terminal

name = "the choosing of the seven"

def go():
    t = Terminal()

    title_delay = 2

    label_delay = 1.5

    speech_delay = 1.5

    move_delay = 0.1

    name_delay = 0.5

    t.draw(
        """
        
        
            The Choosing of the Seven

        
        
        """,
        title_delay
        )

    t.draw(
        """
        Hellenistic Jews              Hebraic Jews
        
            *       *                   *       *
           ***     ***                 ***     ***
            *       *                   *       *
           * *     * *                 * *     * *
        """,
        label_delay
        )

    t.draw(
        """
      Our widows aren't gettting any food!
        
            *       *                   *       *
           ***     ***                 ***     ***
            *       *                   *       *
           * *     * *                 * *     * *
        """,
        speech_delay
        )

    t.draw(
        """
                                    Nuh uh!
        
            *       *                   *       *
           ***     ***                 ***     ***
            *       *                   *       *
           * *     * *                 * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """
                                   You're just fat!
        
            *       *                   *       *
           ***     ***                 ***     ***
            *       *                   *       *
           * *     * *                 * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """
        
        
         The disciples came together to
         fix the problem.
        
        
        """,
        title_delay
        )

    t.draw(
        """
                                   
        
            *       *                   *       *
           ***     ***                 ***     ***
            *       *                   *       *
             * *     * *             * *     * *
        """,
        move_delay
        )

    t.draw(
        """
                                   
        
              *       *               *       *
             ***     ***             ***     ***
              *       *               *       *
             * *     * *             * *     * *
        """,
        move_delay
        )

    t.draw(
        """
                                   
        
              *       *               *       *
             ***     ***             ***     ***
              *       *               *       *
               * *     * *         * *     * *
        """,
        move_delay
        )

    t.draw(
        """
                                   
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        move_delay
        )

    t.draw(
        """
                        What should we do?               
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """
                        KILL THEM ALL            
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay / 2
        )

    t.draw(
        """
                        No, John.            
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """ 
                         *light bulb*         
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )
    t.draw(
        """ 
            Let's assign some people to monitor the food.
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay
        )

    t.draw(
        """ 
            It has to be someone we can live without...
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay
        )

    t.draw(
        """ 
             What's the first thing that comes to your mind:
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """ 
                           "Unneeded"
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 1
        )

    t.draw(
        """ 
                  Procorus!  
        
                **      *           *       *
               **      ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        name_delay
        )

    t.draw(
        """ 
                                 Nicanor!
                                                
                *       *          **       *
               ***     ***          **     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        name_delay
        )

    
    t.draw(
        """ 
                       Good, now: "annoying"
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """ 
                         Timon!  
        
                *       **          *       *
               ***     **          ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        name_delay
        )

    t.draw(
        """ 
                                        Parmenas!
                                                
                *       *           *      **
               ***     ***         ***      **
                *       *           *       *
               * *     * *         * *     * *
        """,
        name_delay
        )

    t.draw(
        """ 
              I agree! How about "want out of here":
        
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.3
        )

    t.draw(
        """ 
             Nicolas! Nicolas!   Nicolas! Nicolas!
        
                **      **         **      **
               **      **           **      **
                *       *           *       *
               * *     * *         * *     * *
        """,
        name_delay + 0.3
        )

    t.draw(
        """ 
         Hey!
        /
                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """ 
             Ok, now let's choose someone for real 

                *       *           *       *
               ***     ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """ 
                I vote Stephen.

                **      *           *       *
               **      ***         ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """ 
                     Yeah, me too
               
                **      **          *       *
               **      **          ***     ***
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """         
                                  Stephen it is!       

                **      **         **      **
               **      **           **      **
                *       *           *       *
               * *     * *         * *     * *
        """,
        speech_delay - 0.5
        )

    t.draw(
        """
        
        
            "This proposal pleased the whole group" (Acts 6:5)

        
        
        """,
        title_delay
        )

    t.finish(t.lineCount)