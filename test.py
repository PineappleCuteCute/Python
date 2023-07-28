print("Hello World!")
print("Welcome to Codelearn.io!")
print(3273+2282)
print("2468 + 1234 =", 2468 + 1234)
print("2468 - 1234 =", 2468 - 1234)
print("2468 * 1234 =", 2468 * 1234)
print("2468 / 1234 =", 2468 / 1234)
'''A simple Python program to display "Hello, World!" on the screen
using Python's print() function'''
#Display Hello World on the screen

# Initialization an integer variable name num_integer
num_integer = 1000
# Initialization a float variable name num_float
num_float = 3.125
# Initialization a string variable name string_var
string_var = 'Codelearn.io'
# Initialization a boolean variable name boolean_var
boolean_var = True

#Print value of each variable
print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)

num_integer = 5000
num_float = 1.2345
string_var = 'Codelearn.io'
boolean_var = False

print(num_integer)
print(num_float)
print(string_var)
print(boolean_var)
name = input()
age = int(input("Nhap so tuoi: "))
print(str(name) + " is " + str(age) + " years old")

a = int(input())
b = int(input())
c=a
a=b
b=c
print("After swap a = " + str(a) + ", b = " + str(b))

'''
Total += a # Using += Operator
print("The Value of the Total after using += Operator is:", Total)
Total -= a # Using -= Operator
print("The Value of the Total after using -= Operator is:", Total)
Total *= a # Using *= Operator
print("The Value of the Total after using *= Operator is:", Total)
Total //= a # Using //= Operator
print("The Value of the Total after using //= Operator is:", Total)
Total **= a # Using **= Operator
print("The Value of the Total after using **= Operator is:", Total)
Total /= a # Using /= Operator
print("The Value of the Total after using /= Operator is:", Total)
Total %= a# Using %= Operator
print("The Value of the Total after using %= Operator is:", Total)
'''


x = int(input())
y = int(input())
z = int(input())
t = int(input())
print("Result evaluation is", (x > y) and (z < t))

age = int(input())
if age < 5: 
    print("Your cat is young")
else : 
    print("Your cat is old")

temperature = int(input())
if temperature >= 100 : 
    print("Stay at home and enjoy a good movie")
elif temperature >= 92 :
    print("Stay at home")
elif temperature == 75 :
    print("Go outside and enjoy the weather")
elif temperature < 0 :
    print("It's cool outside")
else :
    print("Let's go to school")

'''x = int(input())
y = int(input())
z = int(input())

if x % 2 ==0 :
    if y >= 20 :
        print("y is greater than or equal to 20")
    else : 
        print("y is less than 20")
else:
    if z >= 30 :
        print("z is greater than or equal to 30")
    else: 
        print("z is less than 30")'''

'''a = int(input())
b = int(input())
c = int(input())

avg = (a+b+c)/3

if avg > a and avg > b :
    print("The average value is greater than both a and b")
elif avg > a and avg > c:
    print("The average value is greater than both a and c")
elif avg > b and avg > c:
    print("The average value is greater than both b and c")
elif avg > a:
    print("The average value is greater than a")
elif avg > b:
    print("The average value is greater than b")
elif avg > c:
    print("The average value is greater than c")'''

'''age = int(input())

if age <= 0:
    print("This can hardly be true")
elif age == 1:
    print("About 1 human year")
elif age == 2:
    print("About 2 human years")
elif age > 2:
    print("Over 5 human years")'''

'''n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print(min_value)'''

'''n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
sum = 0
for i in list:
    sum += i
print(sum)'''


'''n = int(input())
list = []
for i in range(n):
    list.append(int(input()))
for i in range(len(list)):
    for j in range(i):
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)'''

'''lst = []
n = int(input())

for i in range(n):
    lst.append(int(input()))
lst.sort()
print(lst)'''

'''list = []
n = int(input())

for i in range(n):
    list.append(int(input()))

answer = []
for i in list:
    if i % 2 != 0:
        answer.append(i)
print(answer)'''

'''list = []
n =int(input())

for i in range(n):
    list.append(int(input()))

answer = []
for i in list:
    if i % 5 == 0:
        answer.append(i)

if len(answer) == 0:
    answer = [0]

print(answer)'''


