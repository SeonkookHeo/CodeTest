# Given : 
# n, k : integer, A : array, a_i : element of A
# 1 <= n <= 1,000
# 1 <= a_i <= 1,000,000(0 <= i <= n-1)
# 1 <= k <= 1,000,000
# Question : The frequency of the same elements with k in the array A

# Solution

def solution(n, A, k):
    
    answer = 0
    for a in A:
        if a == k:
            answer += 1
    return answer

# Given : 
# n, i, j, k : integer, A : array, a_i : element of A
# 1 <= n <= 10,000
# 1 <= a_i <= 10,000(0 <= i <= n-1)
# 1 <= i <= j <= n-1
# 1 <= k <= 10
# Question : Multiply k from the ith element a_i to jth element a_j and print the sum of the array A

def solution(n, A, i, j, k):

    for idx in range(i, j + 1):
        A[idx] = A[idx] * k

    return sum(A)

# Given :
# A, B : array, a_i : element of A, b_i : element of B
# a : the case when a_i > b_i
# b : the case when b_i > a_i
# Question : If a > b, print 1. Elif a < b, print 0

def solution(A, B):
    a, b = 0, 0
    for x, y in zip(A, B):
        if x > y:
            a += 1
        elif x < y:
            b += 1

    return int(a > b)
        
# Given :
# n, k : integers, A : 2-dim Array, a_ij : elements of A
# Question : print how many elements in A whose value is k

def solution(n, k, A):
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if A[i][j] == k:
                answer += 1
                
    return answer

# Given :
# n : integer, A : 2-dim n by n Array, a_ij : elements of A
# i1, j1, i2, j2, k : integers
# Multyply k to the elements of A in row i1 ~ i2, column j1 ~ j2

def solution(n, A, i1, j1, i2, j2, k):
    
    answer = 0
    for i in range(i1, i2 + 1):
        for j in range (j1, j2 + 1):
            A[i][j] = A[i][j] * k
    
    for i in range(n):
        answer += sum(A[i])
    
    return answer