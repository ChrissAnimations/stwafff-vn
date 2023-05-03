screen chara_info():

    tag menu

    style_prefix "navigation"

    #add your_image

    textbutton _("Flo"):
        xpos 0.65 ypos 112
        action ShowMenu("flo_info")
    textbutton _("[mcname]"):
        xpos 0.65 ypos 152
        action ShowMenu("koda_info")
    textbutton _("Scarlet"):
        xpos 0.65 ypos 192
        action ShowMenu("scarlet_info")
    textbutton _("Caleb"):
        xpos 0.65 ypos 232
        action ShowMenu("caleb_info")

    textbutton _("Return"):
        style "return_button"

        action Return()
        activate_sound "audio/menu/menu_cancel.wav"

screen flo_info():

    tag menu

    style_prefix "navigation"

    #add your_image




    text "Flo is a fox, That's for sure.\n\nHe's Male, 19 years old, in a relationship with [mcname], and is all around a swell guy to be around.\n\n(more text will be added eventually :P)" xpos 0.1 ypos 112

    textbutton _("Return"):
        style "return_button"

        action ShowMenu("chara_info")
        activate_sound "audio/menu/menu_cancel.wav"

screen koda_info():
    tag menu
    style_prefix "navigation"
    #add your_image
    text "[mcname] is you!\n\nNothing else to be said other than the relationship [they] [have] with Flo." xpos 0.1 ypos 112
    textbutton _("Return"):
        style "return_button"

        action ShowMenu("chara_info")
        activate_sound "audio/menu/menu_cancel.wav"

screen scarlet_info():
    tag menu
    style_prefix "navigation"
    #add your_image
    text "Scarlet might be a fox.\n\nSeems everybody that meets her doesn't seem to like her. Possibly because of how she acts.\n\nI don't know. I'm just a line of text on a screen." xpos 0.1 ypos 112
    textbutton _("Return"):
        style "return_button"

        action ShowMenu("chara_info")
        activate_sound "audio/menu/menu_cancel.wav"

screen caleb_info():
    tag menu
    style_prefix "navigation"
    #add your_image
    text "Caleb is Flo's sibling.\n\nBecause of Caleb's determination to earn money by any means, they decided to\nallow themselves to be a test subject for scientists.\n\nOne such experiment created Caleb's little tail friend, Keith.\n\nKeith is fully sentient, and hasn't been documented on how they work.\n\nMostly because Keith is afraid of people other than Caleb.\n\nOh and another experiment basically made Caleb impossible to reproduce with.\n...which is why they are no longer male.\nBe safe around lasers!" xpos 0.1 ypos 112
    textbutton _("Return"):
        style "return_button"

        action ShowMenu("chara_info")
        activate_sound "audio/menu/menu_cancel.wav"
