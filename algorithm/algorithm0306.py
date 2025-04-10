
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
    
def selectionSort(lst):
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

def binarySearch(val, lst : list): # 이진탐색 함수수
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

def merge(lst1,lst2):
    x,y = 0,0
    newLst = []
    for i in range(len(lst1)+len(lst2)):
        if lst1[x] <= lst2[y]:
            newLst.append(lst1[x])
            x +=  1
        else:
            newLst.append(lst2[y])
            y += 1

def merge2(lst, p, q, r):
    tmp = [None for _ in range(r-p+1)]
    i=p
    j=q+1
    k=0

    print(f"before merge: {lst[p:q+1]}, {lst[q+1:]}")

    while i > q and j > r:
        print(f"before: [{i} = {lst[i]}, {j} = {lst[j]}, tmp = {tmp}")
        if lst[i] < lst[j]:
            tmp[k] = lst[i]
            i+=1
        else:
            tmp[k] = lst[j]
            j+=1
        k+=1
        print(f"after: [{i} = {lst[i]}, {j} = {lst[j]}, tmp = {tmp}")
    if i > q:
        while j <= r:
            tmp[k]=lst[j]
            j+=1
            k+=1
    else:
        while i <= q:
            tmp[k] = lst[i]
            i+=1
            k+=1
    
    for k in  range(r-p+1):
        lst[p+k] = tmp[k]

def mergeSort(lst : list):
    
    lst1 = lst[ : len(lst)//2]
    lst2 = lst[len(lst)//2 : ]
    
    if len(lst1)<=1 and len(lst2)<=1: #종료조건
        return merge(lst1,lst2)

    return merge(mergeSort(lst1),mergeSort(lst2))
    
def mergeSort2(lst : list, p : int, r : int):
    if p >= r:
        return
    q = ( p + r ) // 2
    mergeSort2(lst, p, q)
    mergeSort2(lst, q+1, r)
    merge2(lst, p, q, r)
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

#다음시간 계수, 기수, 버킷 정렬
"""
계수정렬: O(n+k)의 시간복잡도(k는 데이터의 최댓값)

원본 리스트 A
A의 최댓값 길이를 가지고
그 원소들의 등장 횟수를 기록하는 리스트 B
정렬을 기록하는 리스트 C

A 원소의 최댓값을 길이로 하는 B
B의 인덱스에 해당하는 값이 A에 등장한 횟수를 B에 기록함
B 원소의 값들을 이전 원소와 더해 누적합으로 만든다
A 리스트의 뒤에서부터 순회하며 그 값을 인덱스로 B에 있는 원소에 접근한다
B에서 얻은 원소를 C의 인덱스로 사용하여 그 위치에 A의 값을 기록한다
B의 값을 1 감소시킨다

??????????????????

데이터가 정수일때만 가능
최댓값이 매우 클 경우엔 비효율적

기수정렬: O(kn)의 시간복잡도(k는 데이터의 자릿수)
"""

def stepInsertionSort(lst: list, k: int, h: int):
    pass

def shellSort(lst: list):
    pass

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

    lst4 = [random.randint(0,100) for _ in range(10)]
    print(f"merge sort: {lst4}")
    mergeSort2(lst4, 0, len(lst4)-1)
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