###Write a Python program to find those numbers which are divisible by 7
##and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500,2700):
    if(i%7==0)and (i%5==0):
     print(i)
    ##Python program to add two numbers
def fun (a,b):
    sum=a+b
    print(sum)
fun(100,200)

##Maximum of two numbers in Python

def function (a,b):
    if a>b:
        print(a)
    else:
        print(b)
function(5,6)
a=5
b=10
while a>b:
    print(a)
else:
    print(b)


###Python Program for factorial of a number
fact=1
n=int(input(":"))
for i in range(n):
    fact*=n
    n=n-1
print(fact)
 
##Python Program for simple interest

p=1000
t=5
r=2

def simple_interest(p,t,r):
    print(p)
    print(t)
    print(r)
si=p*t*r
print(f"simple interest of amount 1000 for 5 year with 2% rate is {si}")

###Python Program for compound interest
p=1200
T= 2
R=5.4
def cp_in(p,t,r):
    print(p)
    print(t)
    print(r)
a=p*(pow(1+r/100,t))
compound=a-p
print(compound)



##Python program to check whether a number is Prime or not
num=500
if num>1:    
 for i in range(2,num):
      if(num%i)==0:
       print(f"{num}is not a prime number")
       print(i,num//i)
       break
 else:
    print(f"{num}is a prime number")
    
    
    ##Python program to print all Prime numbers in an Interva
prime=[]
def function(a,b):
    for i in range(a,b):
     for j in range(2,int(i/2)+1):
        if i//j==0:
            break
        prime.append(i)
        return prime
    function(2,10)



##Python Program for Program to find area of a circle
pi=3.14
r=float(input("enter the radius of a circle: "))
area_of_a_circle=pi*r*r
print(area_of_a_circle)

