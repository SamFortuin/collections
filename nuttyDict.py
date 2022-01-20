from random import randint
from string import ascii_lowercase,capwords
from shortcuts import intConvert

mmColors = { #starting values
    'rood':0,
    'orange':0,
    'groen':0,
    'blauw':0,
    'geel':0,
    'bruin':0
    }

def createNeg():
    global mmColorsNeg,mmColorsList
    mmColorsNeg = {}
    mmColorsList = list(mmColors)
    for i in range(len(mmColorsList)):
        mmColorsNeg.update({i:mmColorsList[i]})
    #TODO return neg instead of making it global

def mmBagFill(amount):
    for i in range(amount):
        mmColors[mmColorsNeg[randint(0,len(mmColorsList)-1)]] += 1
    #TODO Return a new dict ipv using global
    #*nuttyList type beat

def main():
    createNeg()
    ask = intConvert(input("Hoeveel M&M's?\n"))
    if isinstance(ask,int) and ask > 0:
        mmBagFill(ask)
        for x,y in mmColors.items():
            if y > 0:
                print(f'{y:>2}x {capwords(x)}')
    elif type(ask) != int:
        print('niet een nummer, probeer opnieuw')
        main()
    elif ask < 1:
        print('negatief getal, probeer opnieuw')
        main()

main()