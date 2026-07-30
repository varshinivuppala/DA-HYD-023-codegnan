#numberic datatype-->int,flaot,complex along with boolean
#input formatting -->accepting input from the user-->input()
#Accepting interger input from user
#int(input())-->will accepts any input-->str
'''age=int(input('enter the age:')) #by default input() accepts any input-->str
print(age)
print(type(age))
#float(input()) --> accepts integers,float values
age=float(input('enter the age:'))
print(age)
print(type(age))

#accepting string input from user
name=input("enter the name:")
print(name)
print(type(name))

a=input().split()#by default split() has space
print(a)

#space separeted values
a=input().split()#now you enter the output
print(a)

#comma separated values
a=input('enter the values:').split(',')
print(a)


#list of integers
marks=list(map(int,input('enter the value:').split(',')))
print(marks)

#now we want to accept 2 values from user
marks,salary=map(int,input('enter the value:').split(','))
print(marks)
print(salary)

#single input -->int(input())
#two inputs -->a,b=map(int(input().split(','))
#any number result as list -->a=list(map(int,input().split(',')))

marks=list(map(float,input('enter the value:').split(',')))
print(marks)

#accepting input from user-->int,float->input formatting
#operators -->perators perform operations between values(operands)
#7 types-->arithmetic,assigment,comarision(relationship)
#memberships,identity,logical,bitwise

#arithmetic operators -->arithmetic operations
#=,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3)#float value
#floor division (integer division)-->returns quotient
print(5//3)
#modules-->divisible rules-->returns remainder
print(5%3)
#power (exponential)
print(5**3)


length=int(input('enter the length:'))
breadth=int(input('enter the breadth:'))
area=length*breadth
print(area)

#assigment operators -->assign the values
# =,+=,-=
a=45
print(a)
#update the value of a
a =a+5 #a+=5
print(a)
a=a-5 #a-=5
print(a)

a*=5
print(a)
a/=5
print(a)
a//=5
print(a)
a**=5
print(a)

#comparision operators -->we compare the values -->boolean
# ==(equal to),!=(not equal),>(less than),>(greater than),<=(less than or equal to),>=(greater than or equal to)

age=25
print(age==25) #returns boolean output
print(age!=45)
print(age>=45)
print(age<=45)
print(age<45)
print(age>45)

#membership operator -->in,not in
#it checks for the existance of an object in a collection

marks=[56,45,67,78]
print(45 in marks)
print(35 not in marks)
#print(45 in 455)#type error


#logical operators-->logical decision making -->and,or,not
#and-->all conditions to be satisfied
#or -->any one condition should satisfied

a=(25 in [25,45,65]) and 45<56
print(a)
b=45>56 or 25<=45
print(b)
c=not (True)
print(c)
'''
#identity operators -->check for identity of an object -->id()
#is,is not
a=35
b=35
print(id(a))
print(id(b))
print(a is b)
c=a
print(id(c))
print(c is a)
