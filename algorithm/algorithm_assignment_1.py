import random

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

if __name__ == '__main__':
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