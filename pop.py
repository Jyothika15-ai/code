# prime_nums=[2,3,5,7]
# removed_element=prime_nums.pop()
# print('Removed element:',removed_element)
# print('Updated List:',prime_nums)

#REMOVE
# languages=['python', 'swift', 'C++', 'C', 'Java', 'Rust', 'R']
# languages.remove('python')
# print(languages)

#REVERSING A STRING
# prime_nums=[2,3,5,7]
# prime_nums.reverse()
# print('Reserved List:',prime_nums)

#repeatition
# list1=[12,14,16,18,20]
# print(list1*2)

#concatenation
# list1=[12,14,16,18,20]
# list2=[9,10,32,54,86]
# print(list1+list2)

#length
# list1=[12,14,16,18,20,23,27,39,40]
# print(len(list1))

#iteration
# list1=[12,14,16,39,40]
# for i in list1:
#     print(i)
 
# list=["john", "david", "james", "jonathan"]
# for i in list:
#     print(i)

#membership
# list1=[100,200,500,700]
# print(600 in list)
# print(700 in list)

# list1=[103,675,321,782,200]
# print(max(list1))

# list1=[103,675,321,782,200]
# print(min(list1))

#intersection() method
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# intersection1=set(list1).intersection(list2)
# print(intersection1)
# intersection2=set(list1)&set(list2)
# print(intersection2)

#without using intersection or set keyword
# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# n=[]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             n.append(list2[j])
# print(n)

#FIND THE GREATEST NUMBER WITHOUT USING THE MAX KEYWORD
# a=['12','34','23','9','3']
# greatest=a[0]
# for i in range(len(a)):
#     if a[i] > greatest:
#        greatest=a[i]
# print("The greatest number is:", greatest)

#FIND THE SMALLEST NUMBER WITHOUT USING THE MIN KEYWORD
# a=['12','34','23','9','3']
# smallest=a[0]
# for i in range(len(a)):
#     if a[i] < smallest:
#        smallest=a[i]
# print("The smallest number is:", smallest)

#LIST COMPREHENSION
# numbers=[1,2,3,4,5]
# a=[x**2 for x in numbers]
# print(a)

#MATRIX USING LIST COMPREHENSION
matrix=[[j for j in range(3)] for i in range(3)]
print(matrix)
    