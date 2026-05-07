# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kreswara Redyana")

define a = Character("AS-LEEN")

image k1:
    "images/tbase_01.png"
image a2:
    "images/ybase_01.png"


# The game starts here.

label start:

    play music "lemonade-by-snoozybeats.mp3" fadein 1.0

    scene bg swamp
    
    with fade
    
    show k1
    
    # These display lines of dialogue.

    k "HAIII AS-LEEN."

    k "Are you ready to play this game?"

    hide k1

    show a2

    menu:
        "Pilih jawaban kamu:"

        "Ya":
            a "Lets go frend"

        "Tidak":
            a "Yahhh Sayang Sekali. Aku kecewa bingit"

    stop music fadeout 1.0

    # This ends the game.

    return
