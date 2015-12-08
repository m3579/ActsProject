from art import Terminal

name = "simon the sorcerer"

reference = "Acts 8:9-24"

def go(t):
    
    title_delay = 2

    quick_title_delay = 1

    label_delay = 1

    speech_delay = 1.5

    slow_move_delay = 0.3

    fast_move_delay = 0.2

    t.draw(
        """
     

        Simon the Sorcerer


     
        """,
        title_delay
    )

    t.draw(
        """
          Simon              Crowds
           |                   |
           *           *     *     *     *
          ***         ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        label_delay
    )

    t.draw(
        """
     Hey everybody! Look at me!
                 
          ***          *     *     *     *
           *          ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
     Hey everybody! Look at me!
                 
           *           *     *     *     *
          ***         ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
     Hey everybody! Look at me!
                 
          ***          *     *     *     *
           *          ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
     Hey everybody! Look at me!
                 
           *           *     *     *     *
          ***         ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
        I'm going to do a magic trick!
                 
           *           *     *     *     *
          ***         ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
  
                 
           **          *     *     *     *
           * *        ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
     
                 
           * *         *     *     *     *
           **         ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
        
                 
           **          *     *     *     *
           * *        ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
        
                 
           * *         *     *     *     *
           **         ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
  
                 
           **         *     *     *     *
           **        ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
     
                 
           **         *     *     *     *
           * *       ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
        
                 
           *  *       *     *     *     *
           **        ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
        
                 
           **         *     *     *     *
           *  *      ***   ***   ***   ***
           *           *     *     *     *
          * *         * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
          Bam!
                 
           * *          *     *     *     *
           *           ***   ***   ***   ***
           *  *        *     *     *     *
          * *         * *   * *   * *   * *
        """,
        speech_delay
    )
    
    t.draw(
        """
                               Whoa!
                 
           * *          *     *     *     *
           *           ***   ***   ***   ***
           *  *        *     *     *     *
          * *         * *   * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
     

        "...and all the people, both high and low, gave him their attention
        and exclaimed, 'This man is rightly called the Great Power of God."
        - Acts 8:10
     
        """,
        title_delay + 2
    )

    t.draw(
        """
                                           Hey!
                         
           *           *     *     *             *
          ***         ***   ***   ***           ***
           *           *     *     *             *
          * *         * *   * *   * *           * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                           Hey!
                         
           *           *     *     *             *
          ***         ***   ***   ***           ***
           *           *     *     *             *
          * *         * *   * *   * *         * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                           Hey!
                         
           *           *     *     *           *
          ***         ***   ***   ***         ***
           *           *     *     *           *
          * *         * *   * *   * *         * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                           Hey!
                         
           *           *     *     *           *
          ***         ***   ***   ***         ***
           *           *     *     *           *
          * *         * *   * *   * *       * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                           Philip
                                             |
           *           *     *     *         *
          ***         ***   ***   ***       ***
           *           *     *     *         *
          * *         * *   * *   * *       * *
        """,
        label_delay
    )

    t.draw(
        """
                         Have you guys ever heard of Jesus?
                                             
           *           *     *     *         *
          ***         ***   ***   ***       ***
           *           *     *     *         *
          * *         * *   * *   * *       * *
        """,
        speech_delay
    )

    t.draw(
        """
                             He died for our sins
                                             
           *           *     *     *         *
          ***         ***   ***   ***       ***
           *           *     *     *         *
          * *         * *   * *   * *       * *
        """,
        speech_delay
    )

    t.draw(
        """
                         Isn't *that* a cool trick?
                                             
           *           *     *     *         *
          ***         ***   ***   ***       ***
           *           *     *     *         *
          * *         * *   * *   * *       * *
        """,
        speech_delay
    )

    t.draw(
        """
     

        5 minutes later


     
        """,
        quick_title_delay
    )

    t.draw(
        """
                    Let's all get baptized!
                                             
           *           *     *     *         *
          ***         ***   ***   ***       ***
           *           *     *     *         *
          * *         * *   * *   * *       * *
        """,
        speech_delay
    )

    t.draw(
        """
        Me too!
                                             
           *           *     *     *         *
          ***         ***   ***   ***       ***
           *           *     *     *         *
          * *         * *   * *   * *       * *
        """,
        speech_delay
    )

    t.draw(
        """
     

        "And [Simon] followed Philip everywhere, astonished by the
         great signs and miracles he saw."
        - Acts 8:13

     
        """,
        title_delay + 1
    )

    t.draw(
        """
                Meanwhile, in Jerusalem
                
               *     *            *     *
              ***   ***          ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        title_delay
    )

    t.draw(
        """
       Hey, did you hear? Samaria has accepted the word of God!
                
               *     *            *     *
              ***   ***          ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
                    Really?! This is awesome!
                
               *     *            *     *
              ***   ***          ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
               We need to send someone there
                
               *     *            *     *
              ***   ***          ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
            I vote Peter!      

               **    *            *     *
              **    **           ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        speech_delay - 0.4
    )
    
    t.draw(
        """
            I vote John!      

               **    **           *     *
              **    **           ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        speech_delay - 0.4
    )

    t.draw(
        """
                                    Hey!

               **    **           *     *
              **    **           ***   ***
               *     *            *     *
              * *   * *          * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
     

          In Samaria...


     
        """,
        quick_title_delay
    )

    t.draw(
        """
          John    Peter            New believers
            |       |                 |
            *       *           *     *     *
           ***     ***         ***   ***   ***
            *       *           *     *     *
           * *     * *         * *   * *   * *
        """,
        label_delay
    )

    t.draw(
        """
       They've been baptized, all right
      
            *       *           *     *     *
           ***     ***         ***   ***   ***
            *       *           *     *     *
           * *     * *         * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
    But they haven't received the Holy Spirit yet
      
            *       *           *     *     *
           ***     ***         ***   ***   ***
            *       *           *     *     *
           * *     * *         * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """

      
            *       *           *     *     *
           ***     ***         ***   ***   ***
            *       *           *     *     *
             * *     * *       * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """

      
              *       *         *     *     *
             ***     ***       ***   ***   ***
              *       *         *     *     *
             * *     * *       * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """

      
              *       *         *     *     *
             ***     ***       ***   ***   ***
              *       *         *     *     *
               * *     * *     * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """

      
                *       *       *     *     *
               ***     ***     ***   ***   ***
                *       *       *     *     *
               * *     * *     * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """

      
                *       *       *     *     *
               ***     ***     ***   ***   ***
                *       *       *     *     *
                 * *     * *   * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """

      
                  *       *     *     *     *
                 ***     ***   ***   ***   ***
                  *       *     *     *     *
                 * *     * *   * *   * *   * *
        """,
        fast_move_delay
    )
    
    t.draw(
        """
                           Holy Spirit
                               \/                 
                  * *     * *   *     *     *
                  **      **   ***   ***   ***
                  *       *     *     *     *
                 * *     * *   * *   * *   * *
        """,
        slow_move_delay
    )
    
    t.draw(
        """
                                 Holy Spirit
                                     \/                 
                  * *     * *   *     *     *
                  **      **   ***   ***   ***
                  *       *     *     *     *
                 * *     * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
                                       Holy Spirit
                                           \/                 
                  * *     * *   *     *     *
                  **      **   ***   ***   ***
                  *       *     *     *     *
                 * *     * *   * *   * *   * *
        """,
        slow_move_delay
    )

    t.draw(
        """
                                      
                                                         
                  * *     * *   *     *     *
                  **      **   ***   ***   ***
                  *       *     *     *     *
      *          * *     * *   * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                      
                                                         
     *            * *     * *   *     *     *
     **           **      **   ***   ***   ***
     *            *       *     *     *     *
      *          * *     * *   * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                      
                                                         
     *            * *     * *   *     *     *
     **           **      **   ***   ***   ***
     *            *       *     *     *     *
      * *        * *     * *   * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                      
                                                         
       *          * *     * *    *     *     *
      ***         **      **    ***   ***   ***
       *          *       *      *     *     *
      * *        * *     * *    * *   * *   * *
        """,
        fast_move_delay
    )

    t.draw(
        """
                                      
                                                         
       *          * *     * *    *     *     *
      ***         **      **    ***   ***   ***
       *          *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        fast_move_delay
    )
    
    t.draw(
        """
  Simon the Sorcerer                            
         |                                               
         *        * *     * *    *     *     *
        ***       **      **    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        label_delay
    )

    t.draw(
        """
       Whoa!                       
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
       Lemme make a deal with you:                       
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
    You give me the power to do *that*...                      
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
    I give you a lot of money...                  
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
                  Of course not!              
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
         You cannot buy the kingdom of God with money!        
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
              Go and repent of your sin!
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
           Your heart is not right with God
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
      You are filled with bitterness and are captive to sin
                                                         
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.draw(
        """
    Please pray that nothing you have said
     will happen to me.               
         *        *       *      *     *     *
        ***      ***     ***    ***   ***   ***
         *        *       *      *     *     *
        * *      * *     * *    * *   * *   * *
        """,
        speech_delay
    )

    t.finish(t.lineCount)