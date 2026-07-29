'''
Tokens -->Variables,punctuators
variables-->named memory location,its a placeholder for data
#rules are to be followed

#multi assignment of variables
name,age,place='codegnan','7','hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='--->')
#a,b=2,4,5 #valueerror as too many values to unpack

#reassigning variales
name="codegnan"
a,b=45,1.5
print(a,b)
a,b=b,a #swapping
print(a,b,sep=',')
#a,b=b,c #name error as c is not defined
print(a,b)

#deleting the variable --> del
#del a
#print(a)
#del a,b
#print(a,b)

#punctuators-->[](lists),()(tuples),{}(dict,sets)
name="codegnan";age=7
print(name,age)

#datatypes -->numeric(int,float,complex),boolean,none
#-->sequences -->lists,tuples,sets,strings,frozensets,mapping(dict)
#numeric type -->int,float,complex

#int datatypes-->quantity,age.
age=7
print(age)
print(type(age)) #type --> return the data type

#quantity =03 #it is not allowed because it is 03
#print(quantity)

#float datatype==>temp,salary,price

price=750.24;discount=2.5
print(price,discount)
print(type(price))

#complex data type==>combination of real and imag

i2=4
data=5+i2
print(data)
print(type(data))

data=5+2j
print(data)
print(type(data))
'''
#boolean --> true/false
vaild=True
print(type(vaild))

error=False
print(type(error))

#type casting -->converting one type to another type
#python by default follows implict type(we need not mention the datatype)
#we will go for explit conversion
#every built -in datatype is a built-in function

age=35
print(type(age))
b=float(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)

age=35.4
print(type(age))
b=int(age)
print(b)
c=complex(age)
print(c)
d=bool(age)
print(d)

data=2+5j
print(type(data))
d=bool(data)
print(d)



e=int(float(bool(45)))
print(e)

f= 45+4.5+2+3j+False
print(f)
