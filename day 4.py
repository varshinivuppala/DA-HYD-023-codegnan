'''
Identity operators -->checks the identity of an object -->id()

a=5
b=4
print(id(a))
print(id(b))
c=5
print(id(c))
print(a is c)

a=[1,3,5,7]
b=a
print(id(a))
print(id(b))
c=[1,3,5,7]
print(id(c))
#as we have list (mutable collections)
#ids whereas values are same
print(c is a)#output false
print(c==a)#output true
print(a is not c)


#bitwise operators -->we perform bitwise operations over operands
#&(and),|(or),^(xor),shifing operators(<<,>>)
#number will be converted into binary format

print(5&3)#both 5and 3 to be converted binary and bitwise and is performed
print(5|3)#bitwise OR
print(5^3)#bitwise XOR

print(5 and 3)#here and is logical operator checks for both existances,#returns 5 in above case
print(5 or 3)#returns 3 in this case

#leftshift operator<<,rightshift operator >>
print(5<1)
print(5<<1)

print(5>>1)#convert 15 to binary and perfrom 2 times shifting
print(15>>2)#same 2 times right shift


#input formatting-->input(),int(input()),float(input())
#you know -->single input
#2 or 3 inputs-->map()
#group of integers -->list(map(int,input().split(','))

names=input('enter the names:').split(',')
print(names)

name1,name2=map(str,input("enter the names:").split(','))
print(name1,name2)
'''

#tokens-->numeric datatypes-->operators-->flow of the program
#control block statements -->they control the flow of the program
#when to execute,how to execute
#conditional statements -->if,else,elif(rely on conditions to be executed)
#repetition statements(loops)-->for,while

#conditional statements-->if usage
'''
syntax:
if<condition>:
    statement(s)..


#age=15   already there fixed number
age=int(input('enter the age:')) #user is giving the number
if age>18:
    print('your age is:',age)
    print('you are eligiable')

age=int(input('enter the age:'))
if age>=18 and age in [19,21,20]:
    print('your age is',age)
print(age)


if-else usage as below:
if <condition>:
    statement(s)...
else:
    statement(s)

#vote elibilty->to check his/her voter eligibilty and give access...
age=int(input('enter the age:'))
if age>18:
    print('your age is:',age)
    print('you are eligiable')
else:
    print('you are not eligiable')
'''
#same case let's use only nested-->if,else
age=int(input('enter the age:'))
if age>0:
    if age>18:
        print('you are eligiable')
    else:
        print('you are not eligiable')
else:
    print("you have enterd -ve values/zero enter only +ve")
    

    
