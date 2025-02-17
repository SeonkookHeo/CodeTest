# Given :
# n information
# 1 a : student's number 'a' stands in line
# 2 : a meal ready.
# Question : print the number of the longest line and the last student who don't have meal.
# if there are same number of the longest lines, print the case that the last student's number is the smallest.

import queue

def solution(n, A):
    
    line = queue.Queue()
    mx_line = 0
    last_small_student_num = 0
    
    for i in range(n):
        # When the command is 1, put the student's number
        # Else, pop one student
        if A[i][0] == 1:
            last_student_num = A[i][1]
            line.put(last_student_num)
            if mx_line < line.qsize():
                mx_line = line.qsize()
                last_small_student_num = last_student_num
            elif mx_line == line.qsize():
                if last_small_student_num > last_student_num:
                    last_small_student_num = last_student_num
                
        else:
            line.get()
        
    return mx_line, last_small_student_num

    # Given :
# n information
# 1 a b : student's number 'a' who wants a menu 'b' stands in line
# 2 b : a meal b ready.
# Question : print the lists A, B, and C in ascending.
# A : list of the students who take what they want
# B : list of the students who take meal that they don't want
# C : list of the students who don't take meal.
# if there is no student in list, print 'None'

import queue

def solution(n, S):
    ans = [[] for _ in range(3)]
    line = queue.Queue()
    for i in range(n):
        if S[i][0] == 1:
            line.put([S[i][1], S[i][2]])
        else:
            take_meal = line.get()
            if take_meal[1] == S[i][1]:
                ans[0].append(take_meal[0])
            else:
                ans[1].append(take_meal[0])
    
    for i in range(line.qsize()):
        left_student = line.get()
        ans[2].append(left_student[0])
        
    for i in range(3):
        ans[i].sort()
    return ans

ANS = solution(n, S)
for ans in ANS:
    if len(ans) == 0:
        print('None')
    else:
        for x in ans:
            print(x, end = ' ')
        print()