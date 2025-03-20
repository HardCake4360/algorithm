
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
    
def selectionSort(list):
    if(list is None):
        return
    size = len(list)
    for i in range(size):
        maxIdx = getMaxIdx2(list[:size-i])
        list[size-(i+1)],list[maxIdx] = list[maxIdx],list[size-(i+1)]
    
    return list

def migrate(list:list, here, there):
    temp = list.pop(here)
    list.insert(there,temp)


def insertionSort(list):
    for i in range(len(list)):
        dest = i
        while dest > 0:
            if list[dest]>list[dest-1]:
                break
            dest-=1
        if i == dest:
            continue
        migrate(list,i,dest)
    


if __name__ == '__main__':
    print(oneToN(4))
    print(oneToNRec(10))
    arr=[1,2,3,4,5,6,7,8,9,10]
    print(minMax(arr))
    
    primeList = PrimeListMaker(10)
    print(primeCheck(primeList))

    print(gcd(210,510))
    random.seed(10)
    lst = [9,8,7,6,5,4,3,2,1]
    lst = [random.randint(0,100) for _ in range(10)] #리스트 컴프리헨션
    print(f"{lst}")
    print(selectionSort(lst))

    lst2 = [random.randint(0,100) for _ in range(10)]
    print(lst2)
    insertionSort(lst2)
    print(lst2)
