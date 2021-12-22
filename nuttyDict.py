from random import randint
from string import ascii_lowercase



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

def mmBagFill(amount):
    mmBagList = []
    for i in range(amount):
        mmBagList.append(mmColors[randint(0,2)])
    for i in range(len(mmDict)):
        a = mmBagList.count(mmColors[i])
        mmDict[mmColors[i]] = a
    
    return mmDict
    

def main():
    ask = intConvert(input("Hoeveel M%M's?\n"))
    if isinstance(ask,int) and ask > 0:
        print(*mmBagFill(ask),sep=', ')
        
    elif type(ask) != int:
        print('niet een nummer, probeer opnieuw')
        main()
    elif ask < 1:
        print('negatief getal, probeer opnieuw')
        main()

main()