# a = "Hello World"
# print(a[::-1])

# a[1]="y"
# print(a)

# message='WHAT A NICE DAY'
# print(message.lower())

# message='what a nice day'
# print(message.upper())

# message='everyone is funny'
# print(message.count("e"))

# message='let live people live people die'
# print(message.find("people"))

# txt="chill girl"
# replaced_txt=txt.replace("girl","boy")
# print(replaced_txt)

# num=[21,34,54,12]
# print("before append:",num)
# num.append(15)
# print("after append:",num)

# vowel=['a','e','o','u']
# vowel.insert(2,'i')
# print('list:',vowel)

# prime_num=[2,3,5]
# print("list:",prime_num)
# even_num=[4,6,8]
# print("list2:",even_num)
# prime_num.extend(even_num)
# print("list after append:",prime_num)

a=[]
b=int(input("enter how many values u want to enter: "))
for i in range(0,b):
    value=input("enter ur values: ")
    if value % 2 == 0:
        a.append(value)
        print("even numbers are:", a)
else:
    print("not even")
