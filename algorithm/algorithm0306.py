def oneToN(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

def oneToNRec(n):
    if n == 1:
        return 1
    return n+oneToNRec(n-1)

if __name__ == '__main__':
    print(oneToN(4))
    print(oneToNRec(10))
