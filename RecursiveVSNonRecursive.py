from collections import deque

def palindromeChecker(n):
    d = deque(n)
    for ch in list(d):
        d.append(ch)
    stillEqual = True
    
    while len(d)>1 and stillEqual:
        first = d.popleft()
        last = d.pop()
        
        if first != last:
            stillEqual = False
    return stillEqual
    
palindromeChecker('aba')

def recursivePalindromeChecker(n):
    if len(n)<=1:
        return True
    if n[0] != n[-1]:
        return False
    
    return recursivePalindromeChecker(n[1:-1])
    
recursivePalindromeChecker('absaa')

def recursiveFactorial(n):
    # base case
    if n <= 0: return 1
    
    return n * recursiveFactorial(n-1)
    
recursiveFactorial(5)

def iterativeFactorial(n):
    total = 1
    while n >= 1:
        total *= n
        n -= 1
    return total
    
iterativeFactorial(5)

def recursiveFibonacci(n):
    if n <= 0: return 1
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)
    
recursiveFibonacci(5)

def iterativeFibonacci(n):
    a,b = 1,1
    while n >= 0:
        a,b = b, a+b
        n-=1
    return a

iterativeFibonacci(5)
