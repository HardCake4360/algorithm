#다이나믹 프로그래밍에서 중요한 개념 "memoization"

#피보나치 수열
"""
F(n)=F(n-1)+F(n-2)
F(0)=0
F(1)=1
"""
#top down
memo = None
def fibonacci(n):
    global memo
    if memo is None:
        memo = [-1]*(n+1)
    if n == 0: return 0
    if n == 1: return 1
    if memo[n] != -1:
        return memo[n]
    
    memo[n] = fibonacci(n-1)+fibonacci(n-2)
    
    return memo[n]
    
#bottom up
def fBUp(dest):
    i=2
    val = [0,1]
    while i<=dest:
        i+=1
        val.append(val[i-1]+val[i-2])
    return val[dest] 

#2*n 타일링 문제
"""
0=0
1=1
2=2
3=5 1차: 2번 2차: 1번 3차 2번
4=14  1차: 3번 2차:2번 3차,2번 4차:3번
"""
def tiling(dest):
    if dest<2:
        return dest
    val = [-1 for _ in range(dest+1)]
    val[0]=0
    val[1]=1
    for i in range(2,dest):
        val[i] = (2*val[i-1] + 2*val[i-2])
    return val[dest]

def BABBA(n):
    memo = [-1 for _ in range(n+1)]

    if n == 0:
        return (0,1)
    if n == 1:
        return (1,0)
    
    if memo[n] != -1:
        return memo[n]

    pA,pB = BABBA(n-1)
    memo[n]= (pB, pA + pB)
    return memo[n]

def BABBA_BU(n):
    if n == 0:
        return (0,1)
    val = [-1 for _ in range(n+1)]
    val[0] = (1,0)

    for i in range(1,n+1):
        a,b = val[n-1]
        val[i] = (b,a+b)
    a,b = val[n]
    return (a,b)



if __name__ == "__main__":
    # #fibonacci Sequence
    # for i in range(100):
    #     print(f"{i}:{fBUp(i)}")
    #     memo = None
    # for i in range(10):
    #     print(f"{i}:{tiling(i)}")
    for i in range(10):
        a,b = BABBA(i)
        print(f"{i}: {a},{b}")

    # for i in range(10):
    #     a,b = BABBA_BU(i)
    #     print(f"{i}: {a},{b}")


