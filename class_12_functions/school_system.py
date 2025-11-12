import school_functions as sf
import random as rd

students_grades = []

# generate 100 grades
for _ in range(100):
    students_grades.append(rd.randint(0,10))
    # print(students_grades)

print('The mode from the students grades is:', sf.mode(students_grades))

print('The students\' grades mean is:', sf.mean(students_grades))

print('The students\' grades standard deviation is:', round(sf.std_dev(students_grades), 2))

print('The highest grade is:', sf.high_grade(students_grades))

print('The lowest grade is:', sf.low_grade(students_grades))