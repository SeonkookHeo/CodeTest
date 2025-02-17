# Given :
# A : n pieces of information about objects
# B : m pieces of information to buy objects
# Question : whole price to buy objects

def solution(n, m, A, B):
    
    dic = {}
    for name, price in A:
        dic[name] = int(price)
    
    total_price = 0
    for i in range(m):
        total_price += dic[B[i]]
    return total_price

# Given :
# S : students' name. There may be overlap.
# Question : print the students' name and how many occured in ascending order

def solution(S):
    dic = {}
    for name in S.split():
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    
    ans = list(dic.items())
    ans.sort(key = lambda x: x[0])
    return ans

A = solution(S)
for name, val in A:
    print(name, val)

# Given :
# A : n students' name. There is not overlap.
# B : m students' name. There may be overlap.
# Question : print the students' name which is in A, but not in B by ascending order.

def solution(A, B):
    dic = {}
    for name in B:
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    
    ans = []
    for name in A:
        if name not in dic:
            ans.append(name)
    ans.sort()
    return ans

C = solution(A, B)
for name in C:
    print(name)

# Given :
# A : n phone numbers. 
# B : a phone number
# Question : print how many phone numbers in A different from B but with B as a prefix

def solution(A, B):
    dic = {}
    for phone_number in A:
        for i in range(len(phone_number) - 1):
            prefix = phone_number[:i+1]
            if prefix in dic:
                dic[prefix] += 1
            else:    
                dic[prefix] = 1
    if B in dic:                
        return dic[B]
    else:
        return 0

# Given :
# A : an array saved n positive integers. There may be overlap.
# Question : print the most appearing numbers in A by ascending order.

def solution(n, A):
    dic = {}
    mx = 0
    for a in A:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
        mx = max(mx, dic[a])        
    
    ans = []
    for name, freq in dic.items():
        if mx == freq:
            ans.append(name)
    ans.sort()
    return ans

B = solution(n, A)
for b in B:
    print(b, end = ' ')