# text = input("enter a string")
# reverse = ""
# for i in text:
#     reverse = i + reverse
# print("reversed string is :",reverse)

# n=5
# count=0
# for i in range(0,n):
#     for j in range(0,n):
#         count+=1
#         print(count," ",end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end=" ")

#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(0,n):
#     for j in range(0,i):
#         print(" ",end=" ")
#     for k in range(0,n-i):
#         print("* ",end=" ")
#     print()

# n=5
# a=1
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#         a=a+1
#     print()

#rhombus pattern
# n=6
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end=" ")
#     for k in range(n):
#         print("*",end=" ")
#     print()

#diamond pattern
# n=4
# for i in range(0,n-1):
#     for j in range(0,n-i):
#         print("",end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()
# n=4
# for i  in range(0,n):
#     for j in range(0,i+1):
#         print("",end=" ")
#     for k in range(0,n-i):
#         print("*",end=" ")
#     print()

#Hourglass
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print("* ",end="")
#     print()
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print("",end=" ")
#     for k in range(i+1):
#         print("*",end=" ")
#     print()

# n=4
# for i in range(n):
#     print(" " * (n-i), end="")
#     num=1
#     for j in range(i+1):
#         print(num,end=" ")
#         num=num*(i+j)//(j+1)
#     print()

# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or i==n-1 or j==0 or j==n-1):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#HOLLOW DIAMOND PYRAMID:
# n=4
# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     for j in range(2 * i + 1):
#         if j==0 or j==2 * i:
#            print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(n - 2, -1,-1):
#     print(" " * (n - i -1), end="")
#     for j in range(2 * i + 1):
#         if j == 0 or j == 2 * i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#         print()
            
#hollow full pyramid
# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#              print("",end=" ")
#     for k in range(0,n):
#            if(k==0 or k==i or j==0):
#                   print("*",end=" ")
#            else:
#                   print(" ",end=" ")

#     print()

