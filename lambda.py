# l=lambda a,b:a+b
# print(l(23,67))

# numbers=[45,23,5,6]

# def Fun(num):
#     return num*2

# print(list(map(Fun,numbers)))

# numbers=[45,63,82,9]
# print(list(map(lambda x:x*2, numbers)))

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# print(list(map(is_even,numbers)))
# print(list(filter(is_even,numbers)))

from functools import reduce
s=reduce(lambda a,b:a*b,range(1,6))
print(s)