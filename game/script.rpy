# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kreswara Redyana")

define a = Character("AS-LEEN")

image a1:
    "images/tbase_01.png"


# The game starts here.

label start:


    scene bg swamp
    
    with fade
    
    show a1
    
    # These display lines of dialogue.

    k "HAIII BRODIII."

    k "Are you ready to play this game?"

    # This ends the game.

    return
