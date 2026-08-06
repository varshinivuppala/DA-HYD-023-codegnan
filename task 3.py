'''
p=list(map(int,input().split(',')))
sum=0
for i in p:
    sum=sum+i
print(sum)


password = input("Enter a password: ")

uppercase = 0
lowercase = 0
digits = 0
special = 0

for ch in password:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("\nPassword Analysis")
print("-----------------")
print("Uppercase letters :", uppercase)
print("Lowercase letters :", lowercase)
print("Digits            :", digits)
print("Special characters:", special)



email=input().split()
for i in email:
    print(i.split('@')[1])
'''



a=input().split(',')
for i in a:
    print(isnumeric())



































    
