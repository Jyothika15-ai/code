# a=set()
# print(type(a))

# set1={1,6,4,'abc'}
# print(type(set1))

# Days=set(["Monday","Tuesday","Wednesday","Thursday"])
# print(Days)
# print(type(Days))
# for i in Days:
#     print(i)

#add()method
# Months=set(["January","February","March","April","May","June"])
# print(Months)
# Months.add("July")
# print(Months)

#update(method)
# Months=set(["January","February","March","April","May","June"])
# print(Months)
# Months.update(["July","August"])
# print(Months)

#discard()method
# months=set(["january","february","march",])
# print(months)
# months.discard("january")
# print(months)

#remove() function
# months=set(["january","february","march","april"])
# print(months)

#union of two sets
# Days1={"monday","tuesday","wednesday","thursday"}
# Days2={"friday","saturday","sunday"}
# print(Days1|Days2)

#intersection of two sets
# Days1={"monday","tuesday","wednesday",'thursday'}
# Days2={"monday","tuesday","wednesday"}
# print(Days1&Days2)

#set comparisions
# Days1={"Monday","Tuesday","Wednesday","Thursday"}
# Days2={"Monday","Tuesday"}
# Days3={"Monday","Tuesday","Friday"}
# print(Days1>Days2)
# print(Days1<Days2)
# print(Days2==Days3)

#remove duplicates
# a=[1,1,2,2,3,3,4,4,5,5]
# b=set(a)
# print(b)

# b=set()
# for i in range(5):
#     a=int(input("Enter the numbers: "))
#     b.add(a)
# print(b)

# vowels=set()
# a=input("Enter a sentence: ")
# for i in a.lower():
#     if i in 'aeiou':
#        vowels.add(i)
# print(vowels)

# list1=["january","february","march","april","may"]
# words=set()
# for i in list1:
#     if len(set(i))==len(i):
#         words.add(i)
# print(words)
    