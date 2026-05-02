# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image a1:
    "images/tbase_01.png"


# The game starts here.

label start:


    scene bg swamp
    
    show a1
    
    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
