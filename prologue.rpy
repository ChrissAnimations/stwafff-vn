label prologue:
    scene cg_alleywayawaken1
    mc "Ugh.... my head hurts."
    "I rest my hand against my head."
    mc "It seems like I've got a bad headache..."
    mc "Gawh, this hurts..."
    scene cg_alleywayawaken2
    "A fox person walks up to me, and holds out their hand."
    unk "Hey, are you okay?"
    menu:
        "My head hurts a lot.":
            jump prologue2
        "Not really.":
            jump prologue2
label prologue2:
    unk "Aw, I'm sorry to hear that."
    unk "Here, let me help you up."
    "I grab the foxes hand, and he lifts me up."
    scene alleyway_night
    play music "music/prologue.mp3"
    show flo happy at bottom
    mc "So... who are you?"
    flo "The name's Flo. And you are?"
    mc "[mcname]. My name is [mcname]."
    show flo laugh at bottom
    flo "Gehehe..."
    mc "Are... are you laughing at my name?"
    show flo uh at bottom
    flo "What?!? No!!!"
    show flo smirk at bottom
    flo "I think your name is pretty cute, not gonna lie."
    mc "Oh jeez."
    scene black with dissolve
    stop music
    show logo_1 at center with dissolve
    pause 2.0
    show logo_2 at center
    pause 6.0
    jump ch1_begin
