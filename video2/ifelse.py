# email=input('enter mail:')
# password=input('enter password:')

# if email=='noorxedits@gmail.com' and password=='okay':
#     print('Welcome')
# elif email=='noorxedits@gmail.com' and password!='okay':
#     print('wrong password')
#     print(input('Enter password again:'))
# else:
#     print('error')    

a=int(input('first num:'))
b=int(input('second num: '))
c=int(input('third num: '))

if a<b and b<c:
    print('smallest is',a)
elif b<a and b<c:
    print('smallest is',b)
else:
    print('smallest is',c)        
