week = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']

print('alle dagen in de week:')
print(*week,sep=', ')

print('\nde werkdagen zijn:')
print(*week[:-2],sep=', ')

print('\nde weekend dagen zijn:')
print(*week[5:7],sep=', ')

week.reverse()

print('\nde dagen van de week in omgekeerde volgorde zijn:')
print(*week,sep=', ')

print('\nde werkdagen in omgekeerde volgorde zijn:')
print(*week[2:],sep=', ')

print('\nde weekend dagen in omgekeerde volgorde:')
print(*week[0:2],sep=', ')