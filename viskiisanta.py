#!/usr/bin/python
# coding: utf-8

"""
A random whisky related ramble generator made to protest the fucking idiotic,
paternizing and downright Orwellian alcohol laws in Finland.

The ramblings are in Finnish and consist of three parts in the form of:

  [someone was doing something], 
    when [something else happened], 
      but [conclusion...]

And yes this is indeed a really quick hack. Doesn't need anything fancier.

"""

from random import randrange

firstPart = [
    "Oltiin AVI:n poikien kanssa tinaamassa viskiä",
    "Pyörin omassa ulosteessani viskiexpossa",
    "Kirjotin viskiaiheista blogipostia",
    "Olin tuhoamassa länsimaista yhteiskuntaa viskipäissäni",
]

secondPart = [
    "Viskiexpon pojat tarjos laitonta mallasuutetta"
]

lastPart = [
    "sitten Aluehallintovirasto kielsi kaiken elollisen",
    "koko Viskiexpo joutu linnaan",

]

def getRandFromList(l):
    return l[randrange(len(l))]

def main():
    print getRandFromList(firstPart)+", kun "+getRandFromList(secondPart)+", mutta " + getRandFromList(lastPart)

if __name__ == "__main__":
    main()

