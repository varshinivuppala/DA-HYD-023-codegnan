'''
usage of else with for-->the else keyword will only be executed when the loop is completely done without any break

#for with else

work_log=[0,1,1,1,0,1,0]
#result variable--->longest_streak
longest_streak=0#target variable
current_streak=0
for i in work_log:
    if i==1:
        #print(i)
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
            print(longest_streak)
    else:
        current_streak=0 #streat break
else:
    print(longest_streak)

#in this case when the entire loop execution is done we get result of #else block

#same program with break usage
work_log=[0,1,1,1,0,1,0]
#result variable--->longest_streak
longest_streak=0#target variable
current_streak=0
for i in work_log:
    if i==1:
        #print(i)
        current_streak=current_streak+1
        if current_streak>longest_streak:
            longest_streak=current_streak
            print(longest_streak)
            break
    else:
        current_streak=0 #streat break
else:
    print(longest_streak)


#For-else with notification scenario

notifications=[0,0,0,0]
for notification in notifications:
    if notification==1:
        print('unread notification')
        break
else:
    print('all caught up')


#try to take notifications from user-->list of integers


notifications=list(map(int,input('enter the value:').split(',')))
print('notifications')
for notification in notifications:
    if notification==1:
        print('unread notification')
        break
else:
    print('all caught up')
    '''

#while -->it relies on condition,it will be completely executed until the condition is satisified

'''
syntax while:
 while <condition>:
     statements
'''
'''
while True:
    print('yes')

#it runs an infinite loop we need to press ctrl+C(keyboard interrupt)

i=0 #initialised statement
while i<=10:
    print(i)
    i=i+1 #counter

#get the counter from 10 to 1
i=10
while i>=1:
    print(i)
    i=i-1
#or
i=0
while i<=10:
    print(10-i)
    i=i+1
'''

#banking scenario -->PIN authentication if more that 3 attempts account locked

pin='1234'
max=3
current_attempt=0
while current_attempt<max:
    entered_pin=input('enter the pin:')
    if entered_pin==pin:
        print('login successful')
        break
    else:
        print('enter pin is wrong')
        current_attempt+=1
else:
    print('account locked')
        
    



























    




















