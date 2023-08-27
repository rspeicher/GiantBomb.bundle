from string import maketrans

def cast_from_deck(deck):
    """
    Given a deck which may or may not contain staff members' first names, return an array of full names.

    >>> cast_from_deck("Dan teaches Drew the subtle nuances of grenade handling, nanomachines, and talking to ladies.")
    ['Dan Ryckert', 'Drew Scanlon']

    >>> cast_from_deck("Dan's on the lookout for an animal companion to share his WoW adventures with.")
    ['Dan Ryckert']

    >>> cast_from_deck("Jeff and Brad save the moon from nuke-happy superpowers with the aid of muted trumpets.")
    ['Jeff Gerstmann', 'Brad Shoemaker']

    >>> cast_from_deck("Dr. Doctor gave me the news... I've got a bad case of Brad and Drew.")
    ['Brad Shoemaker', 'Drew Scanlon']

    >>> cast_from_deck("Join the ninja, the skipper, and the douche (and Dan and Brad) as they unravel the mystery of Dead Island. But also escape from it? I think?")
    ['Dan Ryckert', 'Brad Shoemaker']
    """

    cast = []

    # Translate punctuation into spaces.
    deck = deck.translate(maketrans(".,'()", "     "))
    words = deck.split()

    for w in words:
        if w == "Alex":
            cast.append('Alex Navarro')
        elif w == "Austin":
            cast.append('Austin Walker')
        elif w == "Brad":
            cast.append('Brad Shoemaker')
        elif w == "Dan":
            cast.append('Dan Ryckert')
        elif w == "Drew":
            cast.append('Drew Scanlon')
        elif w == "Jason":
            cast.append('Jason Oestreicher')
        elif w == "Jeff":
            cast.append('Jeff Gerstmann')
        elif w == "Patrick":
            cast.append('Patrick Klepek')
        elif w == "Ryan":
            cast.append('Ryan Davis')
        elif w == "Vinny":
            cast.append('Vinny Caravella')
        elif w == "Abby":
            cast.append('Abby Russell')
        elif w == "Ben":
            cast.append('Ben Pack')

    return cast
