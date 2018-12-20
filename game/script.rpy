# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("UNIT 532", who_color="#4e96cc")
define b = Character ("BASTIAN", who_color="#b53827")
define r = Character ("RIKO", who_color="#9a21a5")
define c = Character ("COMPUTER", who_color="#ffffff")
define t = Character ("TERRENCE", who_color="#c2a432")
define w = Character ("???", who_color="#ffffff")
define n = Character (None, window_background= None, what_text_align=0.5)
# The game starts here.
#How to change the background:
## scene bg BACKGROUND_NAME
#How to show a character:

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show b_gj annoyed

    # These display lines of dialogue.
    $ no_box = True
    window hide

    n "It is the year 2066."

    n "Mankind has succeeded in creating artificial beings whose sole purpose is to serve."

    n "I am one of them."

    $ no_box = False
    window show
    voice m1
    m "I am an Elysian Unit, my Model Number is 532, and I am built for the purpose of companionship, in all its shapes and forms."
    voice m2
    m "My workplace, as referred to by humans, is Dollhouse."
    voice m3
    m "To me, it is more than merely a workplace."
    voice m4
    m "Even when I am not with clients, I remain in the establishment with the other biots, who serve humans in the same way."
    voice m5
    m "The time I spend with clients is what I look forward to most."
    voice m6
    m "It’s really the only time I feel something."
    voice m7
    m "I generally don’t find this life dissatisfactory in any way."
    voice m8
    m "After all... What else is there for a biot than to fulfill their primary function?"
    window hide
    $no_box = True
    scene bg dollhouse outside rain
    n "A man in the shadows hurries down a deserted street in the rain."
    n "The bright glare of a sign saying 'Dollhouse' gives him pause."
    n "The man shivers as he repeatedly glances up and down the street."
    return
