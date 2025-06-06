
import random
import heapq

def oneToN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

def oneToNRec(n):
    if n == 1:
        return 1
    return n+oneToNRec(n-1)

def minMax(list):
    min=list[0]
    max=min
    for i in list[1:]:
        if(min>i):
            min=i
            continue
        if(max<i):
            max=i
    return min,max
def getMaxIdx(list):
    maxVal=list[0]
    maxIdx=0
    for i in range(len(list)):
        if(maxVal<list[i]):
            maxVal=list[i]
            maxIdx=i
    return maxIdx

def getMaxIdx2(list:list):
    return list.index(max(list))

def isPrime(x):
    for i in range(2,x//2+1):
        if(x%i == 0):
            return False
    return True

def PrimeListMaker(stop):
    list = [True]*(stop+1)
    list[0],list[1]=False,False
    for i in range(2,stop+1):
        if(list[i] is False):
           continue
        if(isPrime(i)):
            for j in range(2*i,stop,i):
                list[j]=False
                print("%d is false"%j)
        else :
            list[i]=False
            print("%d is false"%i)
    return list

def primeCheck(list):
    sum = 0
    for i in range(len(list)):
        if(list[i]):
            sum+=1
    return sum

def gcd(a,b):
    if(a>b):
        a,b=b,a
    if(b%a is 0):
        return a
    else:
        return gcd(b%a,a)
    
def selectionSort(lst): #선택정렬: 최댓값을 비교해 맨 뒤 원소와 바꿔치기 하는 정렬
    if(lst is None):
        return
    size = len(lst)
    for i in range(size):
        maxIdx = getMaxIdx2(lst[:size-i])
        lst[size-(i+1)],lst[maxIdx] = lst[maxIdx],lst[size-(i+1)]
    
    return lst

def migrate(lst : list, here, there): # 선택한 인덱스(here)를 특정 위치(there)로 이동시키는 함수
    temp = lst.pop(here)
    lst.insert(there,temp)

def insertionSort(lst : list): # 삽입정렬1: 순서 비교를 선택한 인덱스부터 앞으로 진행하는 모델
    for i in range(len(lst)):
        dest = i
        while dest > 0:
            if lst[i]>lst[dest-1]:
                break
            dest-=1
        if i == dest:
            continue
        migrate(lst,i,dest)

def insertionSort2(lst : list): # 삽입정렬2: 순서 비교를 앞에서부터 진행하는 모델
    size = len(lst)
    for i in range(size):
        for j in range(i):
            if i == j:
                continue
            if lst[i]<lst[j]:
                migrate(lst,i,j)
                break

def binarySearch(val, lst : list): # 이진탐색 함수
    start = 0
    end = len(lst)-1
    while start < end:
        mid = (start + end)//2
        if lst[mid] < val:
            start = mid + 1
        else:
            end = mid
    return start

def insertionSort3(lst : list): # 삽입정렬3: 순서 비교를 위해 이진탐색을 이용한 모델
    for i in range(1, len(lst)):
        migrate(lst, i, binarySearch(lst[i], lst[:i+1]))

        
    
def bubbleSort(lst : list):
    size = len(lst)
    while True:
        fin = False
        for i in range(0, size-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                fin =True
        size-=1
        if(fin==False):
            break

# 병합, 퀵, 힙, 셸?쉘? 정렬

def merge(lst, p, q, r):
    tmp = lst[:] #[None for _ in range(r-p+1)]
    i=p
    j=q+1
    k=0

    print(f"before merge: {lst[p:q+1]}, {lst[q+1:]}")

    while i <= q and j<=r:
        if lst[i] <= lst[j]:
            tmp[k] = lst[i]; k += 1; i += 1
        else:
            tmp[k] = lst[j]; k += 1; j += 1
    while i <= q:
        tmp[k] = lst[i]; k += 1; i += 1
    while j <= r:
        tmp[k] = lst[j]; k += 1; j += 1
    i = p; k = 0
    while i <= r:
        lst[i]=tmp[k]; k += 1; i += 1

def mergeSort(lst : list, p : int, r : int):
    if p >= r:
        return
    q = ( p + r ) // 2
    mergeSort(lst, p, q)
    mergeSort(lst, q+1, r)
    merge(lst, p, q, r)
#퀵정렬
"""
정렬이 이미 되어있을 경우 최악
중복 원소가 많을 경우-> 원소들이 한쪽으로 치우쳐 효율 낮아짐
"""
def partition(lst, p, r):
    pivot = lst[r]
    i = p-1
    for j in range(p,r):
        if lst[j] <= pivot:
            i += 1
            lst[i],lst[j] = lst[j],lst[i] #exchange i, j
    lst[i+1],lst[r] = lst[r],lst[i+1] #exchang i+1, r
    return i + 1

def quickSort(lst: list,p: int, r: int):
    if p < r:
        q = partition(lst, p, r)
        quickSort(lst,p,q-1)
        quickSort(lst,q,r)

def part3(lst, p, r):
    if p >= r:
        return
    mid = p
    pivot = lst[random.randint(p,r)]
    
    while mid <= r:
        if lst[mid] < pivot:
            lst[p],lst[mid] = lst[mid],lst[p]
            p += 1
            mid += 1
        elif lst[mid] > pivot:
            lst[r],lst[mid] = lst[mid],lst[r]
            r -= 1
        else:
            mid += 1
    return p, mid

def quick3(lst,p,r):
    if p < r:
        L,R = part3(lst, p, r)
        quick3(lst, p, L-1)
        quick3(lst, R, r)

#힙 정렬
"""
우선순위 큐: 완전 이진트리, 루트 값이 최대 또는 최소, 부모가 자식보다 크거나 같음 또는 작거나 같음이 보장됨
힙 구현이 핵심!
*******시험에 나올수도???*******
힙을 만드는 과정에서 힙의 성립을 확인, 루트에서부터 확인
새로 추가하는과정은 리프노드에 삽입 그리고 성립 확인 -> 업 과정
삭제는 루트의 값을 꺼낼때 루트를 리프노드와 바꿔치기 하고 새 루트부터 성립확인 -> 뭐지? 팝 과정
*******************************
정렬되지 않은 배열 정보-> 완전 이진트리로 변환
이것을 힙정렬 하기 위해 최대 또는 최소 히피파이(힙화) 시킴
최소 또는 최대 힙의 루트 값을 n번 꺼내옴 -> 정렬 완료

heapq를 직접 사용하거나 이미 구현된 힙을 활용하는 코딩 테스트도 있음
"""

def heapSort(lst):
    heap = lst[:]
    heapq.heapify(heap)
    for i in range(len(heap)):
        lst[i] = heapq.heappop(heap)

#셸정렬
"""
삽입 정렬은 거의 정렬이 되어있는 입력에 탁월한 성능
셸 정렬은 삽입 정렬의 성능을 극대화할 수 있게 한 정렬
삽입 정렬에서 원소의 이동 횟수를 극적으로 줄임

n칸 떨어진 원소들 끼리 정렬
n//2칸 떨어진 원소들 끼리 정렬
.... 이 상태의 이점: 거의 정렬이 되어있어 삽입정렬의 효율이 좋은 상태로 만들어줌
1칸 정렬(기존 삽입정렬)
"""

# def sortModule(lst,n):
#     for i in range(n):
#         j = i
#         k = j
#         while j <= len(lst):
#             if k < 0: continue
#             if lst[k]<lst[k-n]:
#                 lst[k], lst[k-n] = lst[k-n],lst[k]
#                 continue
#             j+=n
#     if n <= 1: return
#     sortModule(lst,n//2)
        
    
# def shellSort(lst):
#     n = len(lst)//2
#     sortModule(lst, n)
        
def shellSort(lst):
    l = len(lst)
    n = l//2
    while n > 0:
        for i in range(n,l):
            temp = lst[i]
            j = i - n
            while j >= 0 and lst[j] > temp:
                lst[j + n] = lst[j]
                j -= n
            lst[j + n] = temp
        n//=2

#다음시간 계수, 기수, 버킷 정렬

#계수정렬: O(n+k)의 시간복잡도(k는 데이터의 최댓값)
# 원본 1회 순회 O(n) + 기록된 데이터 순회 O(k) = O(n+k)
""" Counting Sort
원본 리스트 A
A의 최댓값 길이를 가지고
그 원소들의 등장 횟수를 기록하는 리스트 B
정렬을 기록하는 리스트 C

A 원소의 최댓값을 길이로 하는 B
B의 인덱스에 해당하는 값이 A에 등장한 횟수를 B에 기록함
B 원소의 값들을 이전 원소와 더해 누적합으로 만든다
A 리스트를 순회하며 그 값을 인덱스로 B에 있는 원소에 접근한다
B에서 얻은 원소를 C의 인덱스로 사용하여 그 위치에 A의 값을 기록한다
B의 값을 1 감소시킨다

??????????????????

누적합은 어느 값을 어느 위치에 넣을 것인지를 나타냄
누적합이 중요한 요소

데이터가 정수일때만 가능
최댓값이 매우 클 경우엔 비효율적

음수일때는?
최솟값의 절대값만큼 모든 원소에 더한 후 정렬하고 다시 빼면 되지 않을까?
->근데 너무 오래걸림 순회 2번 더해야됨 O(3n+k)

"""

#기수정렬: O(kn)의 시간복잡도(k는 데이터의 자릿수)
"""Radix Sort
0~9까지의 큐
1의 자리에 해당하는 큐로 삽입
2의 자리에 해당....
....n의 자리에 해당하는 큐로 삽입

정렬 완료

코드로 할때는 십진수로 하진 않음(니블?)
문자열같은 자리수가 매우 큰 데이터 정렬에는 비효율적
부동 소수점의 경우 부호, 지수부, 가수부에 대해 각각 기수정렬 필요
"""

#버킷정렬:
"""
기수정렬의 일반화

"""
#시험 팁
"""
과제로 나간 문제들 나올거임
정렬에 대해 잘 아는지 시험할거임
정렬에서 배열을 쓸건지 링크드 리스트 쓸건지 고찰
코드 암기도 필요
"""

#####################################################################중간고사 범위

#그래프
"""
일상에서 사용 사례: 내비게이션, sns 등
각각의 컴퓨터를 노드, 연결된 경로를 엣지라고 하고
최단경로 구하기
np완비 문제같은 것이 많지만 어느정도 작동하고 있음
슈타이너 트리 문제?
문제가 발생했을 때 그것을 그래프 형태로 바꿀 수 있다면
그로인해 얻는 이점은 매우 크다
링크드 리스트는 직접 구현해서 써야함함
"""
#목차
"""
그래프란?
그래프의 표현
*너비 우선 탐색과 깊이 우선 탐색
*최소 신장 트리
*위상 정렬
*최단경로

*: 중요
"""

#다시 그래프로 돌아와서
"""
무향 그래프: Undirected Graph
방향 그래프: Directed Graph
가중 방향 그래프: Weighted Directed Graph
인접 행렬: 그래프가 n*n 행렬 A[][]로 표현된다. 각각 노드가 인접하는지 표현하는 것이 중점
무향/방향 표현 둘다 가능
정점 i, j의 간선 존재 여부를 A[i][j]에 기록
가중치를 기록할 때는 그냥 A[i][j]에 가중치를 기록
"""

#이번 시간에 할것: 그래프의 표현현

if __name__ == '__main__':
    print(oneToN(4))
    print(oneToNRec(10))
    arr=[1,2,3,4,5,6,7,8,9,10]
    print(minMax(arr))
    
    primeList = PrimeListMaker(10)
    print(primeCheck(primeList))

    print(f"{gcd(210,510)}\n")

    lst = [9,8,7,6,5,4,3,2,1]
    lst = [random.randint(0,100) for _ in range(10)] #리스트 컴프리헨션
    print(f"selection sort:{lst}")
    print(f"result        :{selectionSort(lst)}\n")

    lst2 = [random.randint(0,100) for _ in range(10)]
    print(f"insertion sort:{lst2}")
    insertionSort(lst2)
    print(f"result        :{lst2}\n")

    lst2_2 = [random.randint(0,100) for _ in range(10)]
    print(f"insertion sort2:{lst2_2}")
    insertionSort2(lst2_2)
    print(f"result         :{lst2_2}\n")

    lst2_3 = [random.randint(0,100) for _ in range(10)]
    print(f"insertion sort3:{lst2_3}")
    insertionSort3(lst2_3)
    print(f"result         :{lst2_3}\n")

    lst3 = [random.randint(0,100) for _ in range(10)]
    print(f"bubble sort:{lst3}")
    bubbleSort(lst3)
    print(f"result     :{lst3}\n")

    lst4 = [random.randint(0,100) for _ in range(4)]
    print(f"merge sort: {lst4}")
    mergeSort(lst4, 0, len(lst4)-1)
    print(f"result    : {lst4}\n")
    
    lst5 = [random.randint(0,100) for _ in range(10)]
    print(f"quick sort: {lst5}")
    quickSort(lst5, 0, len(lst5)-1)
    print(f"result    : {lst5}\n")

    heap = []
    for _ in range(10):
        heapq.heappush(heap, random.randrange(0,100))
    
    print(f"min heap: {heap}")

    cnt = len(heap)
    B = [heapq.heappop(heap) for _ in range(cnt)]

    print(f"result  : {B}")
    
    lstq = [1,2,3,3,3,4,5]
    print(f"before: {lstq}")
    quick3(lstq,0,len(lstq)-1)
    print(f"after:  {lstq}")
    
    lsth = [random.randint(1,100) for _ in range(10)]
    print(f"heap sort before: {lsth}")
    heapSort(lsth)
    print(f"after           : {lsth}")
    
    lsts = [random.randint(1,100) for _ in range(10)]
    print(f"shell sort before: {lsts}")
    shellSort(lsts)
    print(f"after            : {lsts}")