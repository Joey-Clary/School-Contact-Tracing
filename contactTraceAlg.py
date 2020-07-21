class TraceAlg:
    def __init__(self, studentDataFileName):
        self.studentDataFileName = studentDataFileName
        self.classDict = self.getClassDict()

    def getClassDict(self):
        classDict = {} #ClassName: studName, studName, studName...
        studentDataFile = open(studentDataFileName, 'r')

        for line in studentDataFile:
            studInfo = line.split('\t') #[studName, Hour 1, Hour 2, Hour 3, Hour 4, Hour 5, Hour 6, Hour 7]
            studName = studInfo[0]

            for hourNum in range(1, 8):
                try:
                    classStudents = classDict[studInfo[hourNum] + str(hourNum)]
                except(KeyError):
                    classDict[studInfo[hourNum] + str(hourNum)] = []
                    classStudents = classDict[studInfo[hourNum] + str(hourNum)]

                classStudents.append(studName)
                classDict[studInfo[hourNum] + str(hourNum)] = classStudents

        return classDict
    
    def getClassRoster(self, chkClass):
        return self.classDict[chkClass][:]

    def getStudentSchedule(self, chkName):
        studentDataFile = open(studentDataFileName, 'r')

        for line in studentDataFile:
            studInfo = line.split('\t')
            studName = studInfo[0]
            if studName == chkName:
                return studInfo

    def getPrimaryContacts(self, chkName):
        studInfo = self.getStudentSchedule(chkName)
        del(studInfo[0])
        del(studInfo[7])
        hourNum = 1
        primaryContacts = {}

        for classTeach in studInfo:
            chkClass = classTeach + str(hourNum)
            classRoster = self.getClassRoster(chkClass)
            classRoster.remove(chkName)
            for stud in classRoster:
                try:
                    primaryContacts[stud].append(chkClass)
                except(KeyError):
                    primaryContacts[stud] = [chkClass]
            hourNum += 1
        return primaryContacts

    def getSecondaryContacts(self, chkName, primaryContacts=False):
        if primaryContacts == False:
            primaryContacts = self.getPrimaryContacts(chkName)
        secondaryContacts = {}

        for contactName in primaryContacts:
            studInfo = self.getStudentSchedule(contactName)
            del(studInfo[0])
            del(studInfo[7])
            hourNum = 1

            for classTeach in studInfo:
                chkClass = classTeach + str(hourNum)
                classRoster = self.getClassRoster(chkClass)
                classRoster.remove(contactName)
                for stud in classRoster:
                    try:
                        secondaryContacts[stud].append(contactName)
                    except(KeyError):
                        secondaryContacts[stud] = [contactName]
                hourNum += 1

        return secondaryContacts

    def main(self):
        for i in range(1, 121):
            chkStud = 'Student' + str(i)
            primaryContacts = self.getPrimaryContacts(chkStud)
            secondaryContacts = self.getSecondaryContacts(chkStud, primaryContacts)
            print(chkStud, len(primaryContacts), len(secondaryContacts))
if __name__ == "__main__":
    studentDataFileName = 'C:\\Users\\jclar\\Desktop\\School\\Senior\\School-Contact-Tracing\\demoSchedule.txt'
    trace = TraceAlg(studentDataFileName)
    trace.main()

