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
        speech_delay
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
                    

        



        """,
        title_delay
    )