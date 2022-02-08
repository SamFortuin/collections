from itertools import count
from random import randint
from string import capwords
from shortcuts import *

mmColors = ['rood','orange','groen','blauw','geel','bruin']

def mmBagFill(amount):
    mmBagList = []
    for i in range(amount):
        mmBagList.append(mmColors[randint(0,5)])
    for i in range(len(mmBagList)):
        mmBagList[i] = capwords(mmBagList[i])
    return mmBagList

def sortbag(list):
    list.sort()
    return list

def sortByAmount():
    for i in range(len(mmColors)):
        mmColors.count(i)

def main():
    ask = intConvert(input("Hoeveel M&M's?\n"))
    if isinstance(ask,int) and ask > 0:
        print(*sortbag(mmBagFill(ask)),sep=', ')
    elif type(ask) != int:
        print('niet een nummer, probeer opnieuw\n')
        main()
    elif ask < 1:
        print('negatief getal, probeer opnieuw\n')
        main()
    elif ask > len(mmColors):
        print('zoveel kleuren zijn er niet, probeer opnieuw\n')
        main()

if __name__ == '__main__':
    main()