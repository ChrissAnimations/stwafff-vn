init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("music/menu.mp3", always_unlocked=True)
    mr.add("music/chapter_select.mp3", always_unlocked=True)
    mr.add("music/prologue.mp3", always_unlocked=True)
    mr.add("music/flo_theme.mp3", always_unlocked=True)
    mr.add("music/flo_house.mp3", always_unlocked=True)
    mr.add("music/city_day.mp3", always_unlocked=True)
    mr.add("music/city_sunset.mp3", always_unlocked=True)
    mr.add("music/city_night.mp3", always_unlocked=True)
    mr.add("music/placeholder.mp3", always_unlocked=True)
    mr.add("music/shop_full.mp3", always_unlocked=True)
    mr.add("music/cafe.mp3", always_unlocked=True)
    mr.add("music/placeholder_locked.mp3", always_unlocked=False)

screen music_room:

    tag menu

    frame:
        has vbox

        # The buttons that play each track.
        textbutton "A Simulation" action mr.Play("music/menu.mp3")
        textbutton "Begin From Where?" action mr.Play("music/chapter_select.mp3")
        textbutton "How I Met Him" action mr.Play("music/prologue.mp3")
        textbutton "Fluffy Man (GreenyToaster)" action mr.Play("music/flo_theme.mp3")
        textbutton "It's Ya Boyfie (GreenyToaster)" action mr.Play("music/flo_house.mp3")
        textbutton "Exploring The City" action mr.Play("music/city_day.mp3")
        textbutton "horizon" action mr.Play("music/city_sunset.mp3")
        textbutton "Lunar Lovers (ouch)" action mr.Play("music/city_night.mp3")
        textbutton "He Got Dat Big Energy" action mr.Play("music/placeholder.mp3")
        textbutton "The Baseball Minigame" action mr.Play("music/placeholder.mp3")
        textbutton "alan_cool_epic_song_awesome" action mr.Play("music/placeholder.mp3")
        textbutton "Till We Meet Again" action mr.Play("music/placeholder.mp3")
        textbutton "THE SHOP: RESTOCKED (GreenyToaster + CosmicGem)" action mr.Play("music/shop_full.mp3")
        textbutton "You Never Had A Banana Split? (ouch)" action mr.Play("music/cafe.mp3")
        textbutton "A DELICIOUS SLICE" action mr.Play("music/placeholder_locked.mp3")
        textbutton "OF YOU!!" action mr.Play("music/placeholder_locked.mp3")
        textbutton "It's The Crank" action mr.Play("music/placeholder.mp3")
        textbutton "With Extra Pulp" action mr.Play("music/placeholder.mp3")


        null height 20

        # Buttons that let us advance tracks.
        textbutton "Next" action mr.Next()
        textbutton "Previous" action mr.Previous()

        null height 20


        # The button that lets the user exit the music room.
        textbutton "Main Menu" action ShowMenu("main_menu")

    text "Welcome to the Music Room!\n\nHere you can listen to all of the music used in STWAFFF!" xpos 0.45 ypos 112

    # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "music/menu.mp3")
