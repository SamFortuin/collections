from random import randint,choice
from string import ascii_lowercase,capwords
from shortcuts import intConvert

def addMM(num):
    mmColors = { #starting values
        'rood':0,
        'orange':0,
        'groen':0,
        'blauw':0,
        'geel':0,
        'bruin':0
    }

    bagList = list(mmColors)
    outList,numList = [],[]

    for i in range(num):
        outList.append(choice(bagList))

    outList.sort()

    for y in mmColors:
        for x in range(outList.count(y)):
            mmColors[y] += 1
    
    return mmColors

def sort(inThing):
    if isinstance(inThing,dict):
        a = dict(sorted(inThing.items(), key=lambda item: item[1])) 
        return a #returns the dict after sorting it
    elif isinstance(inThing,list):
        a = inThing.sort()
        return a
    else:
        print('input is not sortable, try again')

def main():
    ask = intConvert(input("Hoeveel M&M's?\n"))
    if isinstance(ask,int) and ask > 0:
        temp = addMM(ask)
        temp = sort(temp)
        for x,y in temp.items():
            if y > 0:
                print(f'{y}x {capwords(x)}')
    elif type(ask) != int:
        print('niet een nummer, probeer opnieuw')
        main()
    elif ask < 1:
        print('negatief getal, probeer opnieuw')
        main()

if __name__ == '__main__':
    main()

#[x] return dict instead of it being global
#[x] add entries to dict
#[x] sort dict based on size