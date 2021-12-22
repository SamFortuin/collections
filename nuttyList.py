from random import randint
from string import ascii_lowercase

mmColors = ['rood','orange','groen','blauw','geel','bruin']

#~210 m&m's in 200g bag 

def intConvert(num):
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

def mmBagFill(amountOfColors):
    mmBagList = []
    for i in range(210):
        mmBagList.append(mmColors[randint(0,amountOfColors-1)])
    return mmBagList

def main():
    ask = intConvert(input("Hoeveel kleuren wilt u in de zak M&M's?\n"))
    if isinstance(ask,int) and ask > 0 and ask <= len(mmColors):
        print(*mmBagFill(ask),sep=', ')
        
    elif type(ask) != int:
        print('niet een nummer, probeer opnieuw\n') 
        main()
    elif ask < 1:
        print('negatief getal, probeer opnieuw\n')
        main()
    elif ask > len(mmColors):
        print('zoveel kleuren zijn er niet, probeer opnieuw\n')
        main()

main()