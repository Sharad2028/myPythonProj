"""

with open("C:\\Users\\shara\\OneDrive\\Desktop\\spark\\pynative.txt","r") as fp:
    line=fp.readlines()

with open("C:\\Users\\shara\\OneDrive\\Desktop\\spark\\pynative1.txt","w") as fp:
    count=0

    for  l in line:
        if count==4:
            pass
        else:
            fp.write(l)
        count+=1
"""
"""
for i in range(1, 11):
    print('Multiplication table of', i)
    for j in range(1, 11):
        # condition to break inner loop
        if i > 5 and j > 5:
            break
        print(i * j, end=' ')
    print('')

"""

"""
i=1
while i <11:
    print(i)
    i+=1
"""
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print(" ")
"""


"""
num=int(input("Enter a Number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

"""

"""
num=int(input("Enter a Number"))
for i in range(1,11):
    print(num*i)

"""
""""
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i%5==0:
        if i>500:
            break
        elif i>150:
            continue
        else:
            print(i)
"""

"""
num=75869
count=0
while num!=0:
    count+=1
    num=num//10
print(count)

"""

"""
for i in range(5,0,-1):
    for j in range(i, 0,-1):
        print(j, end=' ')
    print()

"""


"""
list1 = [10, 20, 30, 40, 50]

len=len(list1)

for i in range(len):
    print(list1[len-i-1])

"""
"""
for i in range(-10,0,1):
    print(i)

"""
"""
for i in range(5):
    print(i)
else:
    print("Done!")

"""
"""
start=int(input())
end=int(input())

print(f"Prime numbers between {start} and {end} are: ")

for i in range(start,end+1):
    for j in range(2,start):
        if i%j==0:
            break
    else:
        print(i)

"""
"""
num1=0
num2=1

for i in range(10):
    print(num1, end=' ')
    res=num1+num2
    num1=num2
    num2=res

"""
"""

num=int(input())
fact=1
for i in range(1, num+1):
    fact=fact*i

print(fact)

"""
"""
n=76542
rev=0
while n!=0:
    r=n%10
    rev= rev*10+r
    n=n//10

print(rev)
"""

"""
start=2
n=5
sum=0
for i in range(n):
    print(start, end= "+")
    sum=sum+start
    start=start*10+2
print("\b","=",sum)

"""
"""
for i in range(1,6):
  for j in range(i):
    print("*",end='')
  print()

for i in range(4,0,-1):
  for j in range(i):
    print("*",end='')
  print()

"""
"""
#functions


def outer_fun(a, b):
  def inner_fun(c, d):
    return c + d

  return inner_fun(a, b)
  return a


result = outer_fun(5, 10)
print(result)

"""
#
# myfamily = {
#   "child1": {
#     "name": "Emil",
#     "year": 2004
#   },
#   "child2": {
#     "name": "Tobias",
#     "year": 2007
#   },
#   "child3": {
#     "name": "Linus",
#     "year": 2011
#   }
# }
#
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict[1]
# print(thisdict)


# def is_palindrom(str1: str):
#    return str1==str1[::-1]
#
# if is_palindrom('naman'):
#   print("p")
# else:
#   print("np")


# def factorial(n):
#    res=1
#    for i in range(n, 0,-1):
#      res=res*i
#
#    return res
#
# print(factorial(5))
#
# n=int(input("Enter a number: "))
# def factorial(n):
#   if n==0:
#     return 1
#   else:
#     return n* factorial(n-1)
#
# print(f"Factorial of {n} is {factorial(n)} ")
#


numbers=[12,5,6,43,9,6]

# def largest_number(numbers):
#   largest=numbers[0]
#   for i in numbers:
#     if i>largest:
#       largest=i
#   return largest
# print(largest_number(numbers))

# def valid_ip(str1:str)->str:
#     flag=False
#     str_liat=str1.split(".")
#     if len(str_liat)==4:
#         for i in str_liat:
#             if i.isdigit():
#                 if int(i) >=0 and int(i) <= 255:
#                     flag=True
#                 else:
#                     flag = False
#                     break
#             else:
#                 flag=False
#                 break
#     else:
#         flag= False
#     return flag
#
# ip='234.35.64.22'
#
# print("Valid IP") if valid_ip(ip) else print("Invalid IP")

# def is_valid(str1):
#     str1_list=str1.split('.')
#     if len(str1_list)!=4:
#         return False
#     for i in str1_list:
#         if i.isdigit()==False:
#             return False
#         if int(i)<0 or int(i)>255:
#             return False
#     return True
#
# print(is_valid('234.54.67.89a'))


# emp_list=[('Ankit',10000),('Rahul',12000),('Sumit',14000),('Dheeraj',21000),('Pavan',11000),('Mohit',13000)]
#
# sum_of_salary=0
# num_of_employee=len(emp_list)
# for i,j in emp_list:
#     sum_of_salary=sum_of_salary+j
#
# avg_of_salary=sum_of_salary/num_of_employee
# mylist=[]
# for k, m in emp_list:
#     if m>=avg_of_salary:
#         mylist.extend([(k,m)])
#
# print(mylist)



# input_list=[1,2,[4,5,6,[4,7,[19,20]],34,56]]
#
# def l_flatten(input_list):
#     l=[]
#     for i in input_list:
#         if type(i) == list:
#            l.extend(l_flatten(i))
#         else:
#             l.append(i)
#     return l
#
# print(l_flatten(input_list))
#
#
# output_list=[]
# def flatten(list2):
#     for i in list2:
#         if type(i)==int:
#             output_list.append(i)
#         else:
#             flatten(i)
#     return output_list
#
# print(flatten(input_list))

arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[3,4,5,6]
arr3=[]

for i in arr1:
    for j in arr2:
        if i==j:
            arr3.append(i)
print(arr3)


def highest(arr1, n):
    for i in range(n):
     highest_num=0
     for i in arr1:
         if i>highest_num:
             highest_num=i
     highest1=arr1.pop(arr1.index(highest_num))
    return highest1

print(highest(arr1, 10))



tup=[(1,2)]
print(tup[0][1])



