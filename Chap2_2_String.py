# Given :
# A : string written by upper and lower alphabets
# Question : B : String with odd-numbered characters of A removed
# print B

def solution(A):
    B = A[1::2]
    return B

# Note : In even case, replace code A[1::2] to A[::2]

# Given :
# A : string written by upper and lower alphabets
# Question : B : String with upper characters of A removed
# print B

def solution(A):
    B = ''
    for a in A:
        if a.islower():
            B += a
            
    return B

# Note : In upper case, use the code isupper()

# Given :
# A : string written by upper and lower alphabets
# Question : B : String with lowercase letters replaced with uppercase letters of A
# print B

def solution(A):
    B = A.upper()
    return B

# Note : In lower case, use the code lower()

# Given :
# A : string written by upper and lower alphabets
# B : string written by upper alphabets. no duplicated characters
# Question : C : String replaced with uppercase letters to lowercase letters in B of A
# print C

def solution(A, B):

    for b in B:
        A = A.replace(b, b.lower())

    return A


# Given :
# A : string which is time that a student studied seperated with blanks
# hour:minute
# Question : the whole time the student studied

def solution(A):
    
    T = 0
    for t in A:
        T += string_to_time(t)
    
    hour = T // 60
    minute = T % 60
    
    ret = ''
    if hour < 100:
        ret = '%02d:%02d'%(hour, minute)
    else:
        ret = '%d:%02d'%(hour, minute)
    return ret
    
def string_to_time(T):
    hour = int(T[0:2])
    minute = int(T[3:5])
    return hour * 60 + minute