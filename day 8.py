'''
tokens-->keywords,identifiers,literals,operator,punctuators,variable
operators-->numberic data(int,floot,boolean,complex)
control flow-->if,elif,for,while
sequences-->strings,lists,sets,tuples,mapping(dict)

#strings-->group of characters,we use single or double or triple quotes
#for representation of strings
#strings are immutable,ordered,indexed collection

name='codegnan'
print(name)
print(type(name))
print(len(name))#len -->returs the number of items in container

#index() --> fetch the object(position) starts at 0 and ends at len(obj)
#we use [] representation
print(name[0])
print(name[5])
print(name[25]) #indexerror-->as its out of range

#negative indexing -->-1 to len(obj)
print(name[-1])#it returns last character
print(name[-3])
print(name[-33])

#slicing-->we can access group of characters(object)
#we use [start:end] #start default-->0,start is included,end is excluted

name='codegnan'
print(name[:]) #returns entire string
print(name[0:])#returns entire string
print(name[:4])#starts ot 0th index befor 4th index
print(name[1:5])
print(name[7:3])#returns empty as string are immutable
#slicing is applicable from lower index to higher index
print(name[:45])#returns till end of the string

name='python'
#print(name[-5:-1])#starts at -5 and ends at -2
print(name[4:6])
print(name[-2:])

name='python'
print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve , -ve,-ve & +ve,-ve all possibilities


#striding -->[start:end:step]

#name:'dataanalysis'
#data-->result
#print(name[:4])
#print(name[4:])
#print(name[-3:])

#print(name[::1])#returns all characters

name:'dataanalysis'
print(name[::2])#includes start to end skipping 1 character
print(name[1:6:3])#[1:6]-->araan-->[1:6:3]-->aa

#tnys
print(name[2::3])
print(name[::-2])
#task:workout with all possibilities of striding on a example

name='codegnan'
#name[3]='w' #strings are immutable

#operations on strings-->indexing,concatenation,repetition
print(name*3)
print('*'*25)#repetition

#concatenation->combining strings

data='sai'+'ram'+ ' '+'god'
print(data)
print('123'*4)#numeric string
print('code' in 'codegnan')
for i in 'codegnan':
    print(i,':')
#in above case we get every character line by line

for i in 'codegnan':
    print(i,end=' ')


name='datacodegnan'
#built-in functions-->len(),min(),max(),sorted()
print(len(name))
print(min(name))#alphabetical order ASCII ordering
print(ord('A')) #it will ASCII Value
print(ord('a'))
print(chr(97))
print(max(name))
print(sorted(name)) #returns a list by sorting all elements
'''


#methods on string -->case-conversions,finding/searching

name='codegnan data'
#case-conversions -->upper(),lower(),title(),capitalize()
a=name.upper()
print(a)
b=name.lower()
print(b)
#capitalize()-->converts first letter to uppercase
c=name.capitalize()
print(c)
d=name.title() #convert every work first letter to uppercase
print(d)


















    






















