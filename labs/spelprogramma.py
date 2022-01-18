from random import randint

spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','Cluedo']

def spelProgramma(inList,minimum=3,maximum=10):
    a = []
    for i in range(randint(minimum,maximum)):
        a.append(f'{i+1}. {inList[randint(0,len(inList)-1)]}')
    return a

print(*spelProgramma(spelList),sep='\n')