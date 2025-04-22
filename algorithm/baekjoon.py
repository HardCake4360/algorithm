import heapq
import random

#11866번
#요세푸스 문제
"""
n:사람 수
k:k-1만큼 뛰어넘고 k번째 수를 제거함
입력 N, K
출력: 요세푸스 순열
"""
def josephusPermutation(n,k):
    lst = [n for n in range(1,n+1)]
    jLst = []
    i=0
    while len(lst) != 0:
        if i == k:
            jLst.append(lst.pop(0))
            i=0
            continue
        else:
            lst.append(lst.pop(0))
        i+=1
    print(jLst)
    
#11279번
#최대 힙
"""
배열에 자연수 X를 삽입
배열에서 가장 큰 값을 Pop()
#배열은 초기에 비어있음
"""
def maxHeap(lst: list, x):
    # maxLst= lst[:]
    # for i in range(len(maxLst)):
    #     maxLst[i] = -maxLst[i]
        
    maxLst = [-lst[i] for i in range(len(lst))]
    maxLst.append(-x)
    heapq.heapify(maxLst)
    print(f"insert value: {x}")
    print(f"pop value: {-heapq.heappop(lst)}")
    lst = [-maxLst[i] for i in range(len(maxLst))]
    print(lst)

if __name__ == "__main__":
    #josephusPermutation(7,2)
    
    lst = [random.randint(1,100) for _ in range(10)]
    x = random.randint(1,100)
    heapq.heapify(lst)
    maxHeap(lst, x)