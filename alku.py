#!/usr/bin/env python
# Tämä on aloitusskripti
import henkilo
import vuodet
# dictionary - sanakirja

henkilötiedot = [
    {"nimi": "Aliisa", "syntymävuosi": 1980}:
    {"nimi": "Bob", "syntymävuosi": 1967},
    {"nimi": "Cecilia", "syntymävuosi": 1920},
]

henkilöiden_lempivärit = {
    "Aliisa": "musta",
    "Bob": "sininen"
}

henkilöiden_lemmikit = {
    "Aliisa": ["Musti"],
    "Bob": ["Tupu", "Hupu", "Lupu"],
}

def henkilölistaus():
    henkilöt = []
    for ht in henkilötiedot:
        h = henkilo.Henkilö({"nimi"}, ht["syntymävuosi"])
        henkilöt.append(h)

    for h in henkilöt:
        print(h.nimi, h.syntymävuosi)
        print(h.nimi, "on", h.ikä(), "vuotta vanha.")
        lemmikit = henkilöiden_lemmikit.get(h.nimi, [])
        for lemmikki in lemmikit:
            print("Lemmikit", lemmikki)
            try:
                print("Lempiväri:",  henkilöiden_lempivärit[h.nimi])
            except KeyError:
                print("Ei lempiväriä tiedossa")
            print("-")    

def pääfunktio():
    syntymävuosi = 1970
    aliisa = henkilo.Henkilö("Aliisa", 1980)
    bob = henkilo.Henkilö(nimi="Bob", syntymävuosi=1967)
    henkilöt = [aliisa, bob]

    for h in henkilöt:
        print(h. nimi, h.syntymävuosi)
        print(h.nimi, "on", h.ikä)


    print(aliisa.nimi)
    print(aliisa.syntymävuosi)

    print(aliisa.ikä())

    print("kutsutaan henkilötiedot-funktiota")
    paluuarvo = bob.tiedot(lempiväri="punainen")
    print("palattiin funktiosta, paluuarvo:", paluuarvo)
    print("Joku syntymävuosi:", syntymävuosi)


pääfunktio()

# teksti = input("Anna luku: ")  # input on funktio

# print(teksti)  # "print" on siis funktio



# if teksti.isdigit():  # isdigit = str luokan metodi (method of str class)
#     luku = int(teksti)
# elif teksti == "yksi":
#     luku = 1
# elif teksti == "kaksi":
#     luku = 2
# elif teksti == "kymppi":
#     luku = 10
# else:
#     print("Ei ollu luku. Varmaan 0 käy sitten.")
#     luku = 0

# print("Luku on:", luku)

# if luku > 10:
#     print("suurempi kuin 10")
# elif luku == 10:
#     print("tasan 10")
# else:
#     print("pienempi kuin 10")