from typing import List, Any


def palendrome(s):
    temp = s[::-1]
    if temp == s:
        print(f"{s} is palendrome")
    else:
        print("not palendrome")

palendrome("aditya")


def armstrong(num):
    sum = 0
    temp = num
    if temp>0:
        digit = temp%10
        sum = sum+(digit**3)
        temp = temp//10

        if num == sum:
            print(f"armstrong number {num}")
        else:
            ("not")

armstrong(153)


for i in range(1,200):
    if i>0:
        sum = 0
        temp = i
        while temp>0:
            digit = temp%10
            sum = sum+(digit**3)
            temp = temp//10
            if i == sum:
                print(f"{i}")
                break

def num():
    if num>0:
        for i in range(2,num):
            if num%i == 0:
                print("not prime")
                break
            else:
                print(f"{num} is prime")
                break


for i in range(0,50):
    if i>0:
        for num in range(2,i):
            if i%num ==0:
                break
            else:
                print(i)
                break

num = int(input("enter number"))
a,b = 0,1
print(a)
while b<num:
    print(b)
    c=a+b
    a=b
    b=c
def string(s):
    lst = []
    temp = s.split(" ")
    for i in temp:
        lst.append(i[0].lower() + i[1:].upper())
    s = '.'.join(lst)
    print(lst)

string("aditya is good")

def string(s):
    string = " "
    b = string.split(" ")
    for i in b:
        str = str + i[0].lower()+i[1:].upper()
    print(str)

s = "aditya mantri is good"


lst = [12,3,27,5,4,9,4]
result = 180
for i in range(len(lst)-2):
    for j in range(len(lst)-1):
        k = int(result/(lst[i] * lst[j]))
        if k in lst[i+2:]:
            print(lst[i],lst[j],k)


lst = [1,5,10,15,20,2]
length = len(lst)
index = 4
input = 500
if index == length:
     lst = lst[:index]+[input]
else:
    lst = lst[:index]+[input]+lst[index:]

print(lst)


string ="aditya is good guy aditya and 50 and 60 of land is under agriculture"
word = 0
num = 0
str =string.split(" ")
for i in str:
     if i.isdigit():
          num =num+1
     else:
          word = word+1
print(word)
print(num)
