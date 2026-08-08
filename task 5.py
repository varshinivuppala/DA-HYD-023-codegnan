'''
#secrect key
s_k=1234
key=int(input('enter the key:'))
while True:
    if s_k==key:
        print('correct')
        break
    
    else:
        print('incorrect')
        key=int(input('enter the key again:'))

#ott
ott=5689
t=int(input('enter the ott:'))
max_a=6
c_a=0
while c_a<max_a:
    if t==ott:        
        print('correct')
        break
    else:
        print('incorrect')
        t=int(input('enter the ott:'))
        c_a=c_a+1
else:
    print('lock')



#food


food=input('enter the food:')
c=0
while food!='exit':
    c=c+1
    food=input('enter the food:')
print('total',c)
'''
game=5
t=int(input('enter the ott:'))
max_a=3
c_a=0
while c_a<max_a:
    if t==game:        
        print('correct')
        break
    else:
        print('incorrect')
        t=int(input('enter the game:'))
        c_a=c_a+1
else:
    print('zero')





































    
    





