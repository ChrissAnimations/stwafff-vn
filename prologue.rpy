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
    flo "Aw, I'm sorry to hear that."
    flo "Here, let me help you up."
    "I grab the foxes hand, and he lifts me up."
    scene alleyway_night
    show flo happy at bottom
    flo "So.... what's your name?"
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
    "I don't know what it was about him."
    "He was so awful at flirting, and tried it on me as soon as we met... and yet..."
    "I found myself falling for him."
    show logo_1 at center with dissolve
    pause 2.0
    show logo_2 at center
    pause 6.0
    jump ch1_begin
