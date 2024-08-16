# Recursion means repetation 
# Recursive funcation is a funcation is calls its self in its own funcation
# 1 thing you need to rembember about Recursive funcation is to add alteast 1 or 2 stop points
# 2nd break the step into small sub steps and start from the smallest step possible 
def factorial(n):
    if n==0:
        return 1 # stop points
    elif n==1:
        return 1 # stop points
    else :
        return n * factorial(n-1)  # here funcation repetaly calls itself 

print(factorial(4))

# calculate fibonacchi series 

def fib(n):
    if n==0:
        return []
    elif n==1:
        return [1]
    elif n==2:
        return [0,1]
    else :
        f=fib(n-1)
        f.append(f[-1]+f[-2])
        return f


print(fib(int(input('Enter number up to which u want to print fibonachi series : '))))

def sum(a):
    if a==1:
        return 1
    elif a==0:
        return 0
    else :
       return a+sum(a-1) # the answer of the previous will send to the sum(a-1)
print(sum(7))

# calculate the sum of the list : 
def sumoflist(l):
    length=len(l)
    b=l.copy()
    Strings=''.join(str(i) for i in l)
    ints=int(Strings)

    if ints==l[0]:
        return l[0]
    else:
        l.pop(length-1)
        l1=[i for i in l]
        l=b.copy()
        print(l)
        # print(length)
        fn= l[length-1]+sumoflist(l1)
        return fn

print('sum of list : ',sumoflist([1,2,3,4,5]))

l=[1,2,3,4,5]
joined_string = ''.join(str(x) for x in l) #'' is a seprator 
print(int(joined_string))

# easy : 
def sum(n):
    if n==0:
        return 0
    else :
        return n+sum(n-1)
print(sum(5))