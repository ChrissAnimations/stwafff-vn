# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define test = Character("Test", color="#000000")
define unk = Character("???")
define mc = Character("[mcname]", color="#ce0000")
define flo = Character("Flo", color="#fe9343")
define clem = Character("Clementine", color="#ffe600")
define alan = Character("Alan", color="#96ff00")
define jay = Character("Jay", color="#c0fdfd")
define scar = Character("Scarlet", color="#e09cff")

image flo angry = "images/flo/angry.png"
image flo blush = "images/flo/blush.png"
image flo confused = "images/flo/confused.png"
image flo devistated = "images/flo/devistated.png"
image flo happy = "images/flo/happy.png"
image flo laugh = "images/flo/laugh.png"
image flo neutral = "images/flo/neutral.png"
image flo sad = "images/flo/sad.png"
image flo smirk = "images/flo/smirk.png"
image flo uh = "images/flo/uh.png"
image flo uwu = "images/flo/uwu.png"
image flo woah = "images/flo/woah.png"

transform center:
    xalign 0.5
    yalign 0.5
transform bottom:
    xalign 0.5
    yalign 0.05
# The game starts here.
label start:
    python:
        mcname = "Koda"
        they = "they"
        They = "They"
        THEY = "THEY"
        them = "them"
        Them = "Them"
        THEM = "THEM"
        their = "their"
        Their = "Their"
        THEIR = "THEIR"
        have = "have"
        Have = "Have"
        HAVE = "HAVE"
    python:
        mcname = renpy.input("What is the desired name?", length=9)
        mcname = mcname.strip()

        if not mcname:
            mcname = "Koda"
    menu:
        "He/Him":
            python:
                they = "he"
                They = "He"
                THEY = "HE"
                them = "him"
                Them = "Him"
                THEM = "HIM"
                their = "his"
                Their = "His"
                THEIR = "HIS"
                have = "has"
                Have = "Has"
                HAVE = "HAS"
            jump pronouns_selected
        "She/Her":
            python:
                they = "she"
                They = "She"
                THEY = "SHE"
                them = "her"
                Them = "Her"
                THEM = "HER"
                their = "hers"
                Their = "Hers"
                THEIR = "HERS"
                have = "has"
                Have = "Has"
                HAVE = "HAS"
            jump pronouns_selected
        "They/Them":
            python:
                they = "they"
                They = "They"
                THEY = "THEY"
                them = "them"
                Them = "Them"
                THEM = "THEM"
                their = "their"
                Their = "Their"
                THEIR = "THEIR"
                have = "have"
                Have = "Have"
                HAVE = "HAVE"
            jump pronouns_selected
        "It/Its":
            python:
                they = "it"
                They = "It"
                THEY = "IT"
                them = "it"
                Them = "It"
                THEM = "IT"
                their = "its"
                Their = "Its"
                THEIR = "ITS"
                have = "has"
                Have = "Has"
                HAVE = "HAS"
            jump pronouns_selected

label pronouns_selected:
    stop music
    scene black
    "..."
    jump what_next
    #jump prologue

    # This ends the game.
    return
