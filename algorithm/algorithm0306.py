
import random

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