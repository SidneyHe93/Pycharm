def menu():
    #prompt the user to enter 1 to invoke enterAllMarksOfAStudentToStorage
    #prompt the user to enter 2 to invoke displayAllReports
    #prompt the user to enter 3 to quit the program

    kbinput = input("Enter 1 to store student details\n" +
        "Enter 2 to display student report\n" +
        "Enter any other key to exit\n")

    if kbinput == '1':
            enterAllMarksOfAStudentToStorage()
    elif kbinput == '2':
            displayAllReports()
    else:
        return

def enterAllMarksOfAStudentToStorage():
    print("The enterAllMarksOfAStudentToStorage function got invoked\n")

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
