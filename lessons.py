#!/usr/bin/python3

from random import randint

'''
There are 6 classes in the school.
Each class has 4 periods every day
Each school week consists of 5 days from Monday till Friday
There are teachers.
Each teacher can only teach one subject.
Each class has 5 subjects. Maths, Physics, Chemistry, Biology and programming. Your program should:
Ask for the number of teachers. (max 10)
The subject they teach.
Their amount of period they teach per month.
Output the timetable for each class.
Each subject must have equal amount of periods in a week. (but not interfere with other classes)
Each class has 1 teacher for 1 subject.
The teachers teaching periods can be higher than what is recommended.
The dropped subjects that if a teacher has extra periods is desired NOT to be maths and physics since 
they are essential part of the education. 
Submit the .py file or the github repository.
'''
classes = dict()
teachers = dict()
teachers_counter = 0
'''
for sub in ("Maths","Physics","Chemistry","Biology","Programming"):
    teachers[sub] = dict()
    print(sub)
    teacher_number = int(input("How many teachers are there for this subject?"))
    teachers_counter += teacher_number
    if teachers_counter > 10:
        print("You can only have a maximum of 10 teachers. Sorry")
        break

    for _ in range (teacher_number):
        name = input("What is the teacher's name?")
        hours = int(input("How many hours does the teacher work per month?"))
        teachers[sub][name] = int(hours/4)
'''

teachers = {'math':{'teacherA':30, 'teacherB':25},
        'physics':{'teacherC':15, 'teacherD':15},
        'chemistry':{'teacherE':15},
        'biology':{'teacherG':15},
        'programming':{'teacherI':15, 'teacherJ':30}}

days = ("Monday:","Tuesday:","Wednesday:","Thursday:","Friday:")
lessons = ("1","2","3","4")

for c in ("Class 1:","Class 2:", "Class 3:", "Class 4:", "Class 5:", "Class 6:"):
    classes[c] = dict()
    for d in days:
        classes[c][d] = dict()
        for les in lessons:
            classes[c][d][les] = None


def filled(exceptClass,day,pair,subj,tutor):
    ''' check if the same subj by tutor exist for other class at the same day and time'''
    if classes[exceptClass][day][pair] is not None:
        return True
    for cl in classes.keys():
        if classes[cl][day][pair] == '{} by {}'.format(subj,tutor):
            return True
    return False


def filling(teachers=teachers, classes=classes, days=days, lessons=lessons):
    for subj, teachs in teachers.items():
        for teacher in teachs.keys():
            for cl, _ in classes.items():
                iter = 0
                while teachers[subj][teacher]:
                    iter +=1 
                    if iter > 2e3: break
                    d = days[randint(0,4)]
                    p = lessons[randint(0,3)]
                    if not filled(cl,d,p,subj,teacher):
                        classes[cl][d][p] = '{} by {}'.format(subj,teacher)
                        teachers[subj][teacher] -= 1
                        break
    return classes


def print_classes(classes=classes):
    non_counter = 0
    for cl,day in classes.items():
        print("\n" + cl)
        for d,pair in day.items():
            print("\n" + d + "\n")
            for p in pair.values():
                print(p)
                if p is None:
                    non_counter += 1
    print('{} None`s'.format(non_counter))


def nons(classes=classes):
    non_counter = 0
    for cl,day in classes.items():
        for d,pair in day.items():
            for p in pair.values():
                if p is None:
                    non_counter +=1    
    return non_counter


if __name__ == "__main__":
    non_counter = i = -1
    nones = []
    while non_counter and i<6:
        i += 1
        classes = filling()
        non_counter = nons()
        nones.append(non_counter)
    print_classes()
    print('min nones is {} from {}'.format(min(nones), nones))
