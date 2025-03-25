#기하 - 1 세 막대
def isTriangle(a,b,c):
    while True:
        end = True
        if a+b<=c:
            c-=1
            end=False
        if b+c<=a:
            a-=1
            end=False
        if a+c<=b:
            b-=1
            end=False
        if end is True:
            break
    return a+b+c

if __name__ == '__main__':
    #기하 - 1 세 막대
    a,b,c = map(int, input().split())
    print(f"largest: {isTriangle(a,b,c)}")