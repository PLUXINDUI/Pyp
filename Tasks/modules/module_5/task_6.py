n=int(input())
fib=[1,1]

k=0
while True:
    k+=1
    fib.append(fib[k-1] + fib[k])

    if n == fib[k]:
        print(k+1)
        break
    elif n < fib[k]:
        print(-1)
        break