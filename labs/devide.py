listOne = ['1','2','3','4','5','6','7','8','9','10']
listTwo = ['2','4','6','8','10','12','14','16','18','20']

def devideAndDisplayList(listOne, listTwo):
    results= []
    for i in range (len(listOne)):
        results.append(int(listOne[i]) / int(listTwo[i]))
    return results

def sort():
    global listOne,listTwo
    listOne.sort()
    listTwo.sort()

def main():
    print('Add lists')
    for i in range(len(listOne)):
        print(f'{listOne[i]:>2} / {listTwo[i]:>2} = {devideAndDisplayList(listOne, listTwo)[i]:>2}')

#print(*addAndDisplayList(listOne, listTwo),sep='\n')
main()