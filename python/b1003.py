N = int(input())

fiboList = [0, 1]
minVal = 1
def Fibo(minVal, maxVal):
    for i in range(minVal+1, maxVal+1):
        fiboList.append(fiboList[i-1] + fiboList[i-2])

for i in range(N):
    n = int(input())
    if(n > minVal):
        Fibo(minVal, n)
        minVal = n
    if (n == 0):
        print(1, 0)
    elif (n == 1):
        print(0, 1)
    else:
        print(fiboList[n-1], fiboList[n])