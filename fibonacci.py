def fibopos(n):
    if n<2:
        return n
    else:
        return fibopos(n-1)+fibopos(n-2)
    
def fiboseries(y):
    a=0
    b=1
    c=[a]
    for i in range(0,y):
        c.append(b)
        #print(b,end="")
        a,b=b,a+b
    print(c)

m=input("Enter 'series' for the Fibonacci series or enter 'pos' for the element in a position: ")
if m=="series":
    print(" ")
    x=int(input("Enter the positive number of terms for the Fibonacci Series: "))
    if x<0:
        print("Invalid input")
    else:
        fiboseries(x)
        
elif m=="pos":
    print(" ")
    q=int(input("Enter a positive number for the position of the Fibonacci series: "))
    p=q-1
    if p<0:
        print("Invalid input")
    else:
        print(fibopos(p),"is found at the position",q)
else:
    print("Invalid input")