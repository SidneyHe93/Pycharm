def main():
    another_student = 'y'
    while another_student == 'y' or another_student == 'Y':
        student_average()
        print()
        another_student = input('do you have another student to enter (y/n) ? ')
    while another_student == 'n' or another_student == 'N':
        student_average_list()
        class_average()
        break

def student_average():
    total = 0.0
    print()
    student_name = input('what is the students name? ')
    print()
    print()
    print(student_name)
    print('-------------------')
    number_of_tests = int(input('please enter the number of tests : '))
    for test_num in range(number_of_tests):
        print('test number', test_num + 1, end='')
        score = float(input(': '))
        total += score
    student_average = total / number_of_tests
    print ()
    print(student_name,"'s average is : ",student_average, sep='')

def student_average_list():
    print ('kahdjskh')

def class_average():
    print ('alsjd')

main()