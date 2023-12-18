"""
A simple text based User Interface (UI) for the Fight for Your Honour game.
"""
import time


class TextUI:
    """
    Initializes a TextUI instance for displaying text-based user interface.

    :return: None
    """

    def __init__(self):
        # Nothing to do...
        pass

    def intro_text(self):
        """
        Displays the introductory story to the user.
        :return: None
        """

        text = ("For years, you have been a loyal knight to your king, serving him faithfully.\n"
                "Your life's purpose is to fight for your king.\n"
                "You have never disobeyed him or allowed anyone to speak ill of him in his absence.\n"
                "Your unwavering loyalty to the king stems from the respect you have for your honour.\n"
                "Throughout your life, you have fought to uphold your honour,\n"
                "always choosing an honourable death over a dishonourable life.\n"
                "Those who dared to insult your honour have not gone unpunished.\n"
                "You are one of the king's most trusted men.\n"
                "However, one day, while you are sleeping, your home's door is broken down,\n"
                "and you are forcibly taken from your bed by the king and other knights.\n"
                "Disappointment is evident on the king's face. In your chamber,\n"
                "you are made to kneel before him, and he asks you the following question:\n"
                "Why have you betrayed me? It seems you have conspired with our enemy to kill me?\n"
                "This question leaves you bewildered, and you explain to the king that you have not betrayed\n"
                "This it is a conspiracy, and you can expose it. The king presents you with two options.\n"
                "1: If you can prove your conspiracy theory and bring the conspirator to the king,\n"
                "dead or alive, your life and honour will be pardoned.\n"
                "2: If you accept the conspiracy and choose to be executed without raising your voice,\n"
                "knowing that your honour remains intact despite the attempt to tarnish it,\n"
                "you may prefer to die with your honour.\n")
        for c in text:
            print(c, end="")
            time.sleep(0.04)

    def textui_print(self, text):
        """
        Displays text to the console.
        :param text: Text to be displayed
        :return: None
        """
        for c in text:
            print(c, end="")
            time.sleep(0.01)

    def game_map_show(self):
        """
        Displays the game map with allowed directions to the console.
        :return: None
        """
        print(
            """
        #You start at f1

        ----------------------------
        |  f1  | f2   | f3   | f4  |
        ----------------------------
        |  f8 |  f7  |  f6  | f5   |
        ----------------------------
        |  f9 | f10  | f11  | f12  |

        Allowed Directions:
        f1: Right or East = f2

        f2: Right or East = f3
            Left or West = f1

        f3: Right or East = f4
            Left or West = f2
        
        f4: Left or West = f3
            Down or South = f5
        
        f5: Left or West = f6
            Up or North = f4
        
        f6: Left or West = f7
            Right or East = f5
        
        f7: Left or West = f8
            Right or East = f6
        
        f8: Down or South = f9
            Left or West = f7
        
        f9: Right or East = f10
            Up or North = f8
        
        f10: Right or East = f11
             Left or West = f9
             
        f11: Right or East = f12
             Left or West = f10
        
        f12: Left or West = f11
        """)
