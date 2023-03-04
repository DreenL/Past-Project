#!/usr/bin/env python
# coding: utf-8

# In[1]:


from random import randrange
from operator import attrgetter
import random
from collections import namedtuple
NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E
alphabet='abcdefghijklmnopqrstuvwxyz'

Student = namedtuple('Student', 'name answers scores total')

#(c.1)
def generate_answers() ->str:
    ''' generates and returns a string of letters representing the correct answers to the test.'''
    n=NUMBER_OF_CHOICES
    result=''
    for i in range(NUMBER_OF_QUESTIONS):
        result+=random.choice(alphabet[0:n])
    return result.upper()
ANSWERS='CADDABACCDACCCBDCBAA'
        
    
#(c.2)#(c.3)
def random_ID()->list:
    '''generate a random ID'''
    n=NUMBER_OF_STUDENTS
    ID=''
    ID_2=[]
    for i in range(n):
        for i in range(8):
            ID+=str(randrange(0,10))
        ID_2.append(ID)
        ID=''
    return ID_2

def right_answer(n:str)->list:
    '''right answer in a list'''
    result_0=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(NUMBER_OF_QUESTIONS):
        if n[i]==ANSWERS[i]:
            result_0[i]=1
    return result_0

def total_right(n:str)->int:
    '''return the number total right'''
    result=0
    for i in range(NUMBER_OF_QUESTIONS):
        if n[i]==ANSWERS[i]:
            result+=1 
    return result




def random_students()->list:
    '''generate random student list'''
    n=NUMBER_OF_STUDENTS
    result=[]
    b=''
    random_answer=''
    c=''
    right_list=[]
    total_1=[]
    for i in range(n):
        for a in random_ID():
            random_answer=generate_answers()
            right_list=right_answer(random_answer)
            total_1=total_right(random_answer)
            b=Student(a,random_answer,right_list,total_1)
        result.append(b)
    return result


def top10_name(n:list)->str:
    '''return top 10 sutdents' name'''
    a=''
    result=sorted(n,key=attrgetter('total'))
    result.reverse()
    result_1=result[:10]
    for i in result_1:
        a+=i.name+'\n'
    return a
print(top10_name(random_students()))

def average_score(n:list)->float:
    '''return the avrage scores'''
    result=0
    result_1=0
    for i in n:
        result+=i.total
    result_1=result/len(n)
    return result_1
print(average_score(random_students()))
        
#(c.4)
def generate_weighted_student_answer(n:str)->str:
    '''generate weighted student answer'''
    a=NUMBER_OF_CHOICES
    result=''
    result+=random.choice(alphabet[0:a]+'{}'.format(2*n))
    return result.upper()

def generate_whole_answer()->str:
    result=''
    result_1=''
    for i in range(len(ANSWERS)):
        result=generate_weighted_student_answer(ANSWERS[i])
        result_1+=result
    return result_1

def random_students2()->list:
    '''create another random list'''
    n=NUMBER_OF_STUDENTS
    result=[]
    b=''
    random_answer=''
    right_list=[]
    total_1=[]
    for i in range(n):
        for a in random_ID():
            random_answer=generate_whole_answer()
            right_list=right_answer(random_answer)
            total_1=total_right(random_answer)
            b=Student(a,random_answer,right_list,total_1)
        result.append(b)
    return result


print(top10_name(random_students2()))

print(average_score(random_students2()))

#(c.5)
def total_student_0_answer_list(n:'number of students')->list:
    '''generate a list of 0'''
    result=[]
    for i in range(n):
        result.append(0)
    return result

def change_answer(n:'list of students')->list:
    '''change 0 to 1, and 1 to 0 in that list'''
    result=[]
    for a in n:
        for i in a.scores:
            if i==1:
                i=0
            elif i==0:
                i=1
        result.append(a.scores)
    return result

def question_weights(n:'list of students')->list:
    result=change_answer(n)
    final_answer=total_student_0_answer_list(NUMBER_OF_STUDENTS)
    for i in range(len(result)):
        for x in range(NUMBER_OF_QUESTIONS):
            if result[i][x] == 1:
                final_answer[x]+=1
    return final_answer[:20]

     
       
def total_get_grade(n:Student)->int:
    '''return the winning total grade'''
    result=0
    for i in range(len(n.scores)):
        if n.scores[i]==1:
            result+=1*350
    return result
def total_lose_grade(n:Student,s:'list of question weights')->int:
    '''return the grade he lost'''
    result=0
    for i in range(len(s)):
        if n.scores[i]==0:
            result+=1*(-s[i])
    return result



def Student_weighted_score(n:Student,s:'list of question weights')->Student:
    '''one student's total scores'''
    i=total_get_grade(n)
    a=total_lose_grade(n,s)
    u=i+a
    n=n._replace(total=u)
    return n
def total_Student_weighted_score(n:list,s:'list of question weights')->list:
    '''return a whole list of total scores'''
    result=[]
    for i in n:
        i=Student_weighted_score(i,s)
        result.append(i)
    return result


    
print(top10_name(total_Student_weighted_score(random_students2(),question_weights(random_students2()))))

print(average_score(total_Student_weighted_score(random_students2(),question_weights(random_students2()))))



#
#
# Part (d)
#
#
print()  
print()
print('---------- Part (d) ----------')
print()
print()



#(d.1a)
def calculate_GPA(n:'list of strings')->float:
    '''return the average of total scores'''
    all_A=n.count('A')
    all_B=n.count('B')
    all_C=n.count('C')
    all_D=n.count('D')
    all_F=n.count('F')
    result=(all_A*4+all_B*3+all_C*2+all_D*1+all_F*0)/len(n)
    return result


#(d.1b)
def calculate_GPAd(n:'list of grades')->float:
    '''return the average of total scores by a dict'''
    grades = {'A+':4,'A':4.0,'A-':3.7,
              'B+':3.3,'B':3.0,'B-':2.7,
              'C+':2.3,'C':2.0,'C-':1.7,
              'D':1.0,'F':0}
    result=grades['A+']*n.count('A+')+grades['A']*n.count('A')+grades['A-']*n.count('A-')+grades['B+']*n.count('B+')+grades['B']*n.count('B')+grades['B-']*n.count('B-')+grades['C+']*n.count('C+')+grades['C']*n.count('C')+grades['C-']*n.count('C-')+grades['D']*n.count('D')+grades['F']*n.count('F')
    result_2=result/len(n)
    return result_2
assert calculate_GPAd(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
            
assert calculate_GPA(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
print(calculate_GPAd(['A', 'A+', 'A-', 'B-', 'A', 'F', 'D']))


#(d.2)
def flatten_2D_list(n:'two-dimensional table')->list:
    result=[]
    for i in n:
        result+=i
    return result

assert flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]

#(d.3a)
L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']
def skip_every_third_item(n:'list of strings')->'each element in the list':
    result=''
    skip = False
    for i in range(len(n)):
        if i%3 == 2:
            skip = True
        if skip:
            skip = False
            continue
        result+= n[i]+'\n'
    return result
print(skip_every_third_item(L))
    
#(d.3b)
def skip_every_nth_item(n:'list of strings',s:int)->'each element expect sth in the list':
    '''takes as input a list and an int (call it n) and prints out each item on the list, except that it skips every nth item.'''
    result=''
    skip = False
    for i in range(len(n)):
        if i%s == s-1:
            skip = True
        if skip:
            skip = False
            continue
        result+= n[i]+'\n'
    return result
print(skip_every_nth_item(L,3))


#(d.4a)
work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(n:'list of workers')->'Dictionary':
    '''return a dict that with values of counts'''
    d = {}
    for i in work_week:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d 
        
print(tally_days_worked(work_week))


#(d.4b)
hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}
def pay_employees(n:'list of workers',s:'Dictionary')->'each employee':
    final=''
    total_hours_each=tally_days_worked(n)
    result={k:total_hours_each[k]*s[k]*8 for k in total_hours_each}
    for i in result:
        final+="{} will be paid ${} for {} hours of work at {} per hour.".format(i,result[i],total_hours_each[i]*8,hourly_wages[i])+'\n'
    return final
print(pay_employees(work_week,hourly_wages))


#(d.5)
def reverse_dict(n:'Dictionary')->'Dictionary':
    result={v: k for k, v in n.items()}
    return result
print(reverse_dict({'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'}))


# In[ ]:




