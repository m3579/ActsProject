from art import Terminal

name = "peter heals a lame beggar"

def go():

    t = Terminal()

    title_delay = 2

    walk_delay = 0.2

    label_delay = 1

    speech_delay = 1.5

    jump_delay = 0.4

    t.draw(
        """


                Peter Heals a Lame Beggar
                
        


        """,
        title_delay
    )

    t.draw(
        """
            |
            |
            |  
            |            *     *
            |*          ***   ***
            |*           *     *
            |***        * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |            *     *
            |*          ***   ***
            |*           *     *
            |***       * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |           *     *
            |*         ***   ***
            |*          *     *
            |***       * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |           *     *
            |*         ***   ***
            |*          *     *
            |***      * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |          *     *
            |*        ***   ***
            |*         *     *
            |***      * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |          *     *
            |*        ***   ***
            |*         *     *
            |***     * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |         *     *
            |*       ***   ***
            |*        *     *
            |***     * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |         *     *
            |*       ***   ***
            |*        *     *
            |***    * *   * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            |
            |  
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        walk_delay
    )
    
    t.draw(
        """
            |
            |   <- Temple Gate
            | Beggar
            | \/     *     *
            |*      ***   ***   <- Peter and John
            |*       *     *
            |***    * *   * *
        """,
        label_delay
    )

    t.draw(
        """
            |
            |
            |Please...
            |\/      *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay - 0.5
    )

    t.draw(
        """
            |
            |
            |Please...give me money
            |\/      *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |       (What should we do?)
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |       (We don't have money!)
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |    (Right, but let's tell him in a cool way)
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |       Silver and gold I do not have!
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |        (Now what?)
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |      (I don't know!)
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |      In the name of Jesus, walk!
            |        *     *
            |*      ***   ***
            |*       *     *
            |***    * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            |
            | 
            |     
            |        *     *
            |*      ***   ***
            |*       *     *
            |***   * *    * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            |       *      *
            |*     ***    ***
            |*      *      *
            |***   * *    * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            |       *      *
            |*     ***    ***
            |*      *      *
            |***  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            |      *       *
            |*    ***     ***
            |*     *       *
            |***  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            |     *        *
            |*   ***      ***
            |*     *       *
            |***  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            |     *        *
            |* * ***      ***
            |*     *       *
            |***  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            | *    *       *
            |*** ***      ***
            |*    *        *
            |***  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            | *    *       *
            |***  ***     ***
            | *    *       *
            |* *  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |         (I should have thought of that!)
            | *    *       *
            |***  ***     ***
            | *    *       *
            |* *  * *     * *
        """,
        speech_delay - 0.5
    )

    t.draw(
        """
            |
            |   Yes!
            | *   
            |***   *       *
            | *   ***     ***
            |***   *       *
            |     * *     * *
        """,
        jump_delay
    )

    t.draw(
        """
            |
            |  Yes!
            |     
            | *    *       *
            |***  ***     ***
            | *    *       *
            |* *  * *     * *
        """,
        jump_delay
    )

    t.draw(
        """
            |
            |  I can walk!
            | *    
            |***   *       *
            | *   ***     ***
            |***   *       *
            |     * *     * *
        """,
        jump_delay
    )
   
    t.draw(
        """
            |
            |  I can walk!
            |     
            | *    *       *
            |***  ***     ***
            | *    *       *
            |* *  * *     * *
        """,
        jump_delay
    )

    t.draw(
        """
            |
            | 
            |     
            | *    *       *
            |***  ***     ***
            | *    *       *
             * *  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            | *    *       *
            |***  ***     ***
              *    *       *
             * *  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
            | *    *       *
             ***  ***     ***
              *    *       *
             * *  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
            |     
              *    *       *
             ***  ***     ***
              *    *       *
             * *  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
                 
              *    *       *
             ***  ***     ***
              *    *       *
             * *  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
         Hey everybody!        
              *    *       *
             ***  ***     ***
              *    *       *
           * *    * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
         Hey everybody!        
            *      *       *
           ***    ***     ***
            *      *       *
           * *    * *     * *
        """,
        walk_delay
    )
    
    t.draw(
        """
            |
            | 
         Hey everybody!        
           *       *       *
          ***     ***     ***
           *       *       *
          * *     * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
       I can walk!       
           *       *       *
          ***     ***     ***
           *       *       *
         * *      * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
       I can walk!       
          *        *       *
         ***      ***     ***
          *        *       *
         * *      * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
       I can walk!       
          *        *       *
         ***      ***     ***
          *        *       *
        * *       * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
       I can walk!       
         *         *       *
        ***       ***     ***
         *         *       *
        * *       * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
       I can walk!       
         *         *       *
        ***       ***     ***
         *         *       *
                  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
            |
            | 
       I can walk!       
                   *       *
        *         ***     ***
                   *       *
                  * *     * *
        """,
        walk_delay
    )

    t.draw(
        """
                    

                At Solomon's Colonnade



        """,
        title_delay
    )

    t.draw(
        """
                    
            How did you heal him?
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                           It wasn't through our power!
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
               Yeah, no duh.
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay - 0.5
    )

    t.draw(
        """
                    
        (Wait, I didn't know what)
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay - 0.5
    )

    t.draw(
        """
                    
            (Be quiet!)
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay - 0.5  
    )

    t.draw(
        """
                    
                              It's through Jesus's!
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )
    
    t.draw(
        """
                    
                           God is glorifying Him
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                           because you killed Him.
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                           You had acted in ignorance,
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                           but now is your chance to repent.
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                         All of the prophets have spoken
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                           about this day.
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
          So you're just going to let the beggar
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
          run around everywhere?
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                              Why not?
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
                    
                       It can't possibly be of any consequence!
              *     *           *     * 
             ***   ***         ***   ***
              *     *           *     *
             * *   * *         * *   * *  
        """,
        speech_delay    
    )

    t.draw(
        """
            Prison
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***    <- Pharisees     
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        label_delay
    )
    
    t.draw(
        """
           I *told* you not to let him run around everywhere!
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***        
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        speech_delay
    )

    t.draw(
        """
           But what did you say?
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***        
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        speech_delay
    )

    t.draw(
        """
           Go away John.
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***        
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        speech_delay
    )

    t.draw(
        """
          It wouldn't be of any consequence!
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***        
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        speech_delay
    )

    t.draw(
        """
          Well, what do you think NOW?
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***        
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        speech_delay
    )

    t.draw(
        """
       At least some people believed.
         ------------------
          |  *|   |   | * |   *
          | **|   |   |***|  ***        
          |  *|   |   | * |   *
          | * |   |   |* *|  * *
        """,
        speech_delay
    )

    t.draw(
        """
                                                     
                 The Game of Life                               
                              
                       
            Church Member Count: 5000

                                                 
    
                    
                                     
                                    
        """,
        speech_delay
    )

    t.draw(
        """
                                                     
                 The Game of Life                               
                              
                       
            Church Member Count: 5000

                                                 
            Your progress for today is:
            
                                     
                                    
        """,
        speech_delay
    )

    t.draw(
        """
                                                     
                 The Game of Life                               
                              
                       
            Church Member Count: 5000

                                                 
            Your progress for today is: Good, but you are in prison.
            
                                     
                                    
        """,
        speech_delay
    )

    t.draw(
        """
                                                     
                
                To be continued...
            

                                     
                                    
        """,
        speech_delay
    )

    t.finish(t.lineCount)