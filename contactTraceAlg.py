class TraceAlg:
    def __init__(self, studentDataFileName):
        self.studentDataFile = open(studentDataFileName, 'r')

    def getData(self):
        classDict = {} #ClassName: studName, studName, studName...

        for line in self.studentDataFile:
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

    def main(self):
        classDict = self.getData()
        for className in classDict:
            print(classDict[className])

if __name__ == "__main__":
    studentDataFileName = 'C:\\Users\\jclar\\Desktop\\School\\Senior\\School-Contact-Tracing\\demoSchedule.txt'
    trace = TraceAlg(studentDataFileName)
    trace.main()

