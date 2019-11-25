def menu():
    allStudentMarks = {}  #Storage for all students marks. The storage is in the form of a dictionary data structure
    while True:
        kbinput = input("Enter 1 to store student details\n" +
                    "Enter 2 to display student report\n" +
                    "Enter any other key to exit\n")

        if kbinput == '1':
                allStudentMarks = enterAllMarksOfAStudentToStorage(allStudentMarks)
        elif kbinput == '2':
                displayAllReports()
        elif kbinput!='1' and kbinput != '2':
            break #break could have been replaced by return. return returns the control flow out of the function
                    #break breaks the control out of the loop

def enterAllMarksOfAStudentToStorage(allStudentMarks):
    while True:
        fname = input("Enter a student's full name\n")
        if searchStudentMarks(fname,allStudentMarks ):
            print(fname, " already exists in the system. Choose another name\n")
        else:
            break

    #enter valid marks for DF Report; valid marks range: 0 to 20
    while True:
        dfReportMarks = input("enter marks for DF Report; valid marks range: 0 to 20\n")
        dfReportMarks = float (dfReportMarks)
        if dfReportMarks >= 0 and dfReportMarks <= 20:
            break

    #enter valid makrs for Project: valid marks range: 0 to 30
    while True:
        projectMarks = input("enter marks for Project; valid marks range: 0 to 30\n")
        projectMarks = float (projectMarks)
        if projectMarks >= 0 and projectMarks <= 30:
            break

    while True:
        finalExamMarks = input("enter marks for Final Exam; valid marks range: 0 to 50\n")
        finalExamMarks = float (finalExamMarks)
        if finalExamMarks >= 0 and finalExamMarks <= 50:
            break

    studentMarks = [dfReportMarks, projectMarks, finalExamMarks]

    allStudentMarks[fname] = studentMarks

    ##temporary code to display current dictionary content
    for k, v in allStudentMarks.items():
        print ("Student ", k, "'s marks are \n")
        for m in v:
            print(m, "\t")

    return allStudentMarks


def displayAllReports():

    kbinput = input("Enter 1 to get DF Report Marks\n" +
            "Enter 2 to get Project Marks\n" +
            "Enter 3 to get Final Exam Marks\n" +
            "Enter 4 to get Overall Marks\n" +
            "Enter 5 to get Selected Student Marks\n" +
            "Enter 6 to get to Menu\n")

    if kbinput == 1:
            getBelowAvgDfReportMarksReport()
    if kbinput == 2:
             getBelowAvgProjectMarksReport()

    if kbinput == 3:
            getBelowAvgFinalExamMarksReport()

    if kbinput == 4:
            getBelowAvgOverallMarksReport()

    if kbinput == 5:
            displaySelectedStudentsMarks()

    if kbinput == 6:
            return

def getBelowAvgDfReportMarksReport():

    print("The getBelowAvgDfReportMarksReport got invoked\n")

def getBelowAvgProjectMarksReport():
    print("The  getBelowAvgProjectMarksReport got invoked\n")

def getBelowAvgFinalExamMarksReport():
    print("The getBelowAvgFinalExamMarksReport got invoked\n")

def getBelowAvgOverallMarksReport():
    print("The getBelowAvgOverallMarksReport got invoked\n")

def displaySelectedStudentsMarks():
    print("The displaySelectedStudentsMarks got invoked\n")


def searchStudentMarks(newNameOfStudent, allStudentsStorage):
    return  newNameOfStudent in allStudentsStorage


menu()