label cc_cameo:
    "I approach the nearby coffee seller."
    show fiona neutral
    fiona "Here to get some coffee?"
    "I point at the apples that the wolf woman was selling."
    show fiona grump
    fiona "Really?"
    "I shamefully nod my head in response."
    "I then give the wolf woman enough money for two apples."
    "She gives them to me, angrily."
    mc "Thank you."
    "As I walk back to Flo, I hear the woman speak again."
    fiona "You know this is a coffee shop, right?"
    "I feel bad."
    menu:
        "Get some coffee too.":
            jump getcoffee
        "I have to save my money.":
            jump ignorefiona
