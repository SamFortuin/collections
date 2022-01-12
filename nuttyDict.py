from random import randint
from string import ascii_lowercase,capwords

mmColors = { #starting values
    'rood':0,
    'orange':0,
    'groen':0,
    'blauw':0,
    'geel':0,
    'bruin':0
    }

def createNeg():
    global mmColorsNeg
    mmColorsNeg = {}
    mmColorsList = list(mmColors)
    for i in range(len(mmColorsList)):
        mmColorsNeg.update({i:mmColorsList[i]})

def intConvert(num):
    num = num.lower()
    numConvert1 = False
    numConvert2 = True
    alphabet = list(ascii_lowercase) #creates list of lowercase alphabet
    for i in range(10):
        if str(i) in num:
            numConvert1 = True
    for x in range(26):
        if alphabet[x] in num: #checks if a letter is present in the arg
            numConvert2 = False
    if numConvert1 and numConvert2: #skips == True because of if logic
        return int(num)
    else:
        return num

def mmBagFill(amount):
    for i in range(amount):
        mmColors[mmColorsNeg[randint(0,5)]] += 1
    

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