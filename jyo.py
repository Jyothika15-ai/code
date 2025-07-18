# n=5
# for i in range(n):
#     for j in range(n):
#         if i == 0:
#             print("*", end="")
#         elif i < n - 1 and j == n - 1:
#             print("*", end="")
#         elif i == n - 1 and j <= n // 2:
#             print("*", end="")
#         elif i >= n // 2 and j == 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#         print()

#factorial of a number
# a=int(input("Enter a number: "))
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
# print(f"factorial of {a} is {fact}")

# a=int(input("Enter a number: "))
# count=1
# while(count<=a):
#     print(count,end=" ")
#     count+=1
'''
a=int(input("Enter a number: "))
ifact=1
count=1
while(fact>=0):
      fact=fact*i
      print(fact, " ")
      '''
    
    
    

'''
def greetings(name,age):
      print("hello",name,age)
greetings("nithin",25)
greetings("yadhu",26)
greetings("parthiv",23)'''
'''
def total (*n):
    print(sum (n))
total(56,34,25,)'''

'''
def greeting(**student):
    print(f"hello {student ["name"]} you are {student["age"]}years ")

greeting(age=27,name="nithin")'''
'''
def sample(a,b):
    return a,b 
c,b=sample(7,3)
print(c,b)
'''

c=10
def sample ():
    global c
    c=c+1
'''
sample()
print(c)'''

def fact(num):
    if num==1:
        return num
    else:
        return num*fact(num-1) 

print(fact(5))      