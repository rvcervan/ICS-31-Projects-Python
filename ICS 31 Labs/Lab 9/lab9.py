# Raul Cervantes 77825705  Jennifer Manivanh 95332154. ICS 31 Lab sec 3. Lab asst 9.

print('--part c1--')
import random

CHOICES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 6
WEIGHTED = 1

def generate_answers()-> str:
    Key = ''
    for i in range(NUMBER_OF_QUESTIONS):
        Answers = random.choice(CHOICES[:NUMBER_OF_CHOICES])
        Key += Answers
    return Key

##print(generate_answers())

print()
print('--part c2--')
from collections import namedtuple

Student = namedtuple('Student', 'ID answers')

def random_students() -> 'list of Student':
    students = []
    for i in range(NUMBER_OF_STUDENTS):
        ID = random.randrange(1000000000, 9999999999)
        answers = generate_answers()
        student = Student(ID, answers)
        students.append(student)
    return students
##print(random_students())

print()
print('--part c3--')

Student = namedtuple('Student', 'ID answers scores total')

Key = generate_answers()
##Key = generate_weighted_student_answer(CHOICES[WEIGHTED])

def score(student_answers:list) -> list:
    score = []
    for i in range(NUMBER_OF_QUESTIONS):
        if Key[i] == student_answers[i]:
            score.append(1)
        else:
            score.append(0)
    return score
##print(score(generate_answers()))

def totals(scores: list) -> int:
    total = 0
    for i in scores:
        total += i
    return total

##print(total([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]))
        

def random_students() -> 'list of Student':
    students = []
    for i in range(NUMBER_OF_STUDENTS):
        ID = random.randrange(1000000000, 9999999999)
        answers = generate_answers()
        scores = score(answers)
        total = totals(scores)
        student = Student(ID, answers, scores, total)
        students.append(student)
    return students

def student_score(s: Student) -> int:
    return s.total

def score_total(student: list) -> int:
    totals = 0
    x = sorted(random_students(), key = student_score, reverse = True)[0:10]
    for i in x:
        totals += i.total
    return totals

    

##print(sorted(random_students(), key = student_score, reverse = True)[0:10])
##x = sorted(random_students(), key = student_score, reverse = True)[0:10]
##print(score_total(x)/len(sorted(random_students(), key = student_score, reverse = True)[0:10]))

print()
print('--part c4--')

def generate_weighted_student_answer(s: str) -> str:
    return random.choice(CHOICES[:NUMBER_OF_CHOICES] + s*NUMBER_OF_CHOICES*2)



##print(generate_weighted_student_answer('A'))

def random_students2() -> 'list of Student':
    students = []
    for i in range(NUMBER_OF_STUDENTS):
        answers = []
        ID = random.randrange(1000000000, 9999999999)
        for x in range(NUMBER_OF_QUESTIONS):
            answers.append(generate_weighted_student_answer(Key[x]))
        scores = score(answers)
        total = totals(scores)
        student = Student(ID, answers, scores, total)
        students.append(student)
    return students
##random_students2()
##print(random_students2())

##print(sorted(random_students2(), key = student_score, reverse = True)[0:10])
##x = sorted(random_students2(), key = student_score, reverse = True)[0:10]
##print(score_total(x)/len(sorted(random_students2(), key = student_score, reverse = True)[0:10]))

print()
print('--part c5--')
#compare the 0s and 1s and for every 0 add on the score total of what that question
#is worth.
def question_weights(s: 'list of Students') -> list:
    total = []
    for q in range(NUMBER_OF_QUESTIONS):
        num_correct = 0
        for student in s:
            if student.scores[q] == 0:
                num_correct += 1
        total.append(num_correct)
    return total

def Student_weighted_score(s: Student, weights: list) -> Student:
    new_total = 0
    for i in range(NUMBER_OF_QUESTIONS):
        if s.scores[i] == 1:
            new_total += weights[i]
    return s._replace(total = new_total)

x = random_students2()
weights = question_weights(x)
##print(Student_weighted_score(x[0],weights))

print()
print('--part d1a--')

def calculate_GPA(s: 'list of strings') -> float:
    total = 0
    for i in s:
        if i == 'A':
            total += 4
        elif i == 'B':
            total += 3
        elif i == 'C':
            total += 2
        elif i == 'D':
            total += 1
        elif i == 'F':
            total += 0
    return total/len(s)

##print(calculate_GPA(['A','A','A','A']))

print()
print('--part d1b--')

def calculate_GPA2(s: 'list of strings') -> float:
    grade = {'A':4,'A-':3.7,'B+':3.3,'B':3,'B-':2.7,'C+':2.3,'C':2,'C-':1.7,'D+':1.3,'D':1,'D-':0.7,'F':0}
    total = 0
    for i in s:
        total += grade[i]
    return total/len(s)
##print(calculate_GPA2(['A','A','A','A-']))

print()
print('--part d2--')

def flatten_2D_list(l: list) -> list:
    new = []
    for i in l:
        new.extend(i)
    return new
##print(flatten_2D_list([[1,3,2],[3,5,1],[7,5,1]]))

print()
print('--part d3a--')

L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise',
     'correctly', '534523423', 'this', 'should', '1044323', 'be', 'readable']

def skip_every_third_item(L: list):
    for i in range(len(L)):
        if not (i+1)%3 == 0:
            print(L[i])

##skip_every_third_item(L)

print()
print('--part d3b--')

def skip_every_nth_item(L: list, n: int):
    for i in range(len(L)):
        if not (i+1)%n == 0:
            print(L[i])

##skip_every_nth_item(L, 3)

print()
print('--part d4a--')

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(L: list):
    names = {}
    for i in L:
        if i not in names.keys():
            names[i] = 1
        else:
            names[i] += 1
    return(names)
        
##print(tally_days_worked(work_week))

print()
print('--part d4b--')

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00,
                'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}

def pay_employees(worker: dict, wage: dict):
    for i in worker:
        print(('{} will be paid ${:.2f} for {} hours of work at ${:.2f} per hour.'.format(i, (8*worker[i])*wage[i], 8 * worker[i], wage[i])))

##pay_employees(tally_days_worked(work_week), hourly_wages)
    
print()
print('--part d5--')

din = {3:1, 4:2, 5:7}

def reverse_dict(d: dict) -> dict:
    new_dict = {}
    for key in d:
        new_dict[d[key]] = key
    return new_dict

##print(reverse_dict(din))
    
    

    
    
    
        
    

            



