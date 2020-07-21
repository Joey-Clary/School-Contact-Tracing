import random

f = open('C:\\Users\\jclar\\Desktop\\School\\Senior\\School-Contact-Tracing\\demoSchedule.txt', 'w+')

def getSchedule():
    classList = []
    for i in range(7):
        choice = random.randint(0, len(teacherList) - 1)
        classList.append(teacherList.pop(choice))
        print(teacherList)
    return classList
    
for stud in range(120):
    teacherList = ['Todaro', 'Mcguire', 'Mcdowell', 'Clements', 'Soileau', 'Handrop', 'Miller', 'Moyers', 'Hall', 'Ayers']
    classList = getSchedule()
    clStr = 'Student' + str(stud + 1) + '\t'
    for cl in classList:
        clStr = clStr + cl + '\t'
    f.write(clStr + '\n')
f.close()