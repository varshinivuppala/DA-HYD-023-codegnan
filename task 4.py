'''
write a python program to calculate the innings of the batsman and boundaries,total scores

n=[4,6,1,0,2,4,0,6]
runs=list(map(int,input().split()))
t=b=d=0
for i in runs:
    t+=i
    if i==4 or i==6:
        b+=1
    elif i==0:
        d+=1
print('t',t)
print('b',b)
print('d',d)

#write the program using while loop to unlock the patten atleast 5 attempts       
current_pin=2356
max_attempts=5
current_attempts=0
while current_attempts < max_attempts:
    pin=input('enter the pin:')
    if pin==current_pin:
        print('you are login succenfully')
        print('phone unlock')
        break
    else:
        current_attempts +=1
        print('wrong pin entered')
        
if current_attempts==max_attempts: 
    print('lock')
        

atm_pin=2356
max_attempts=3
current_attempts=0
while current_attempts < max_attempts:
    pin=input('enter the pin:')
    if pin==atm_pin:
        print('you are login succenfully')
        print('phone unlock')
        break
    else:
        current_attempts +=1
        print('wrong pin entered')
        
if current_attempts==max_attempts: 
    print('lock')


'''

movies = ["Salaar", "Bahubali", "KGF"]

for i in range(len(movies)):
    print(i + 1, ".", movies[i])























