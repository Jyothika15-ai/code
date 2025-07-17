# capital_city={"Nepal":"Kathmandu","Italy":"Rome"}
# print(capital_city)
# for i in capital_city:
#     print(capital_city[i])

# capital_city={"Nepal":"Kathmandu","England":"London"}
# print("Initial Dictionary:",capital_city)
# capital_city["Nepal"]="Tokyo"
# print("Upadated Dictionary:",capital_city)

# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print("Initial Dictionary:",student_id)
# student_id[112]="Stan"
# print("Updated Dictionary:",student_id)

# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print(student_id[111])
# print(student_id[113])

# student_id={111:"Eric",112:"Kyle",113:"Butters"}
# print("Initial Dictionary", student_id)
# del student_id[111]
# print("Updated Dictionary", student_id)

#Iterating through a dictionary
# squares={1:1,3:9,5:25,7:49,9:81}
# for i in squares:
#     print(squares[i])

# keys=['name','age','city','address']
# values=['Alice',30,'New York']

# my_dict=list(zip(keys, values))
# print(my_dict)

#function
# def square(num):
#           return num**2
# object_=square(6)
# print("The square of the given number is: ", object_)

# def square(num):
#         print(num**2)
#         square(6)

#calling a function
# def a_function(string):
#     "This prints the value of length of string"
#     return len(string)

#calling the function we defined
# print(a_function("Functions"))
# print(a_function("Python"))

#function to calculate square of a number
# def square(num):
#     return num*num

# result=square(5)
# print("Squares: ", result)

#with argument without return type
# def greet(name):
#     print("Hello",name+"!")
# greet("Anu")

#without arugument with return type
#function that returns a welcome message
# def get_message():
#     return "Welcome to python programming!"
# msg=get_message()
# print(msg)

#without argument without return type
#function to print from 1 to 5
# def print_numbers():
#     for i in range(1,6):
#         print(i)

# print_numbers()

#default arguments
# def function(n1,n2=20): 
#     print("number 1 is: ",n1)
#     print("number 1 is: ",n2)
# print("Passing only one argument")
# function(30)

# keyword argument
# def function(n1, n2):
#     print("number 1 is: ", n1)
#     print("number 2 is: ", n2)
# print("Without using keyword")
# function(n2=50,n1=20)

#odd or even
# def my_is(num):
#     if num%2==0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")
# b=int(input("Enter the number"))
# my_is(b)

#Factorial of a number
# def is_factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     print(fact)
# a=int(input("Enter the number: "))
# is_factorial(a)

# def is_even(num):
#     if num%2==0:
#       return True
#     else: 
#       return False
# a=int(input("enter the number: "))
# c=is_even(a)
# if c:
#    print(a, "is even")

#sample
# def fun(name,age):
#     print(f"My name is {name} and my age is {age}")
# fun("jyo","20")

# def Display(**a):
#     print(f"Hi {a['name']} Welcome to {a['course']} course")
#     Display(name,age)

    


    
          
   




