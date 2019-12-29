#!/usr/bin/python3

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

for c in ("Class 1:","Class 2:", "Class 3:", "Class 4:", "Class 5:", "Class 6:"):
    classes[c] = dict()
    for d in ("Monday:","Tuesday:","Wednesday:","Thursday:","Friday:"):
        classes[c][d] = dict()
        for les in ("1","2","3","4"):
            classes[c][d][les] = None



def filled(exceptClass,day,pair,subj,tutor):
    ''' check if the same subj by tutor exist for other class at the same day and time'''
    if classes[exceptClass][day][pair] is not None:
        return True
    for cl in classes.keys():
        if classes[cl][day][pair] == '{} by {}'.format(subj,tutor):
            return True
    return False
                
nextClass = False
for subj, teachs in teachers.items():
    for teacher in teachs.keys():
        if teachers[subj][teacher]:
            for cl, day in classes.items():
                if teachers[subj][teacher]:
                    for d, pair in day.items():
                        if not nextClass:
                            for p in pair.keys():
                                if not filled(cl,d,p,subj,teacher):
                                    classes[cl][d][p] = '{} by {}'.format(subj,teacher)
                                    teachers[subj][teacher] -= 1
                                    nextClass = True
                                    break
                        else:
                            nextClass = False
                            break

if __name__ == "__main__":
    for cl,day in classes.items():
        print("\n" + cl)
        for d,pair in day.items():
            print("\n" + d + "\n")
            for p in pair.values():
                print(p) 