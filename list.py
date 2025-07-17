# prime_nums=[2,3,5,7]
# removed_element=prime_nums.pop(2)
# print('Removed Element:', removed_element)
# print('Updated List:', prime_nums)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(a)):
#     if i<=len(a)-1:
#         if a[i]%2!=0:
#             a.pop(i)
# print("List:",a)

a=[]
while True:
       print("1.Add")
       print("2.Remove")
       choice=int(input("Enter the choice: "))
       if choice==1:
             num=int(input("Enter a number: "))
             a.append(num)
             print("Added Element: ", num)
             print("Current List:",a)
       elif choice==2:
              b=int(input("Enter a number to remove: "))
              for i in range(len(a)):
                  if i<=len(a)-1:
                    if a[i]==b:
                      a.pop(i)
                      print(a)
            
              



