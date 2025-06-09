import heapq

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

#0605 수업내용
"""
-기말 대책
연습문제 풀어보기
다빈치 코딩 알고리즘에 나온거
전부 코드 시험
그래프 내용
중간고사 내용은 안나옴

점화식으로 표현 가능한가? -> 다이나믹 프로그래밍으로 풀기 + memoization + bottom up 방식
다이나믹 프로그래밍 부분에서 최소 하나는 나옴옴
"""
#평범한 배낭 문제
def solve(n,k):
    if k<0 or k<W[n]: return 0
    case1 = solve(n-1, k) +V[n]
    case2 = solve(n-1,k)
    return max(case1,case2)

#동전 문제
def coin(coins:list, val):
    coins[1]*val/coin[1] + coins[2]*val/coin[2] + ... + coins[n]*val/coins[n]

    for coin in coins:
        for i in range(0,val/coin+1):
            coin*i

#조약돌 문제
#RGB거리

"""
-시험에 나올만한 문제
분할정복: 쿼드 트리 문제
백 트래킹: 근손실 문제
누적합: 다이나믹 프로그래밍 적 해석
그리디 알고리즘
"""

#쿼드 트리 문제
"""
00 01 02 03
10 11 12 13
20 21 22 23
30 31 32 33

00 01 02 03
04 05 06 07
08 09 10 11
12 13 14 15
"""
def QuatroTre(image:list, size: int):
    pass

def quadTree(image:list, size: int):
    lst = toString(image)
    upperLeft = [0,2,8,10]
    temp = []
    result = []
    for pivot in upperLeft:
        temp.append(lst[pivot])
        temp.append(lst[pivot+1])
        temp.append(lst[pivot+size])
        temp.append(lst[pivot+size+1])
        if '0' in temp and '1' in temp:
            result.append(toTuple(temp))
        else:
            result.append(temp.pop())
        temp.clear()
    
    return result    
    
def toString(lst: list):
    temp = []
    for line in image:
        for c in line: 
            temp.append(c)
    return temp

def toTuple(lst):
    return (lst[0],lst[1],lst[2],lst[3])

#백 트래킹: 근손실 문제
def mLoss(N,K,kit:list):
    m = 500
    
    

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
    
    image = ["0011",
             "0011",
             "1101",
             "1110"
             ]
    print(quadTree(image,4))

    kit = [3, 7, 5]
    mLoss(3,4,kit)
