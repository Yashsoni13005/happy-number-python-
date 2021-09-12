#Python program to check if the given number is Happy Number

x=int(input('enter a number'))
print(x)

def happy(x):
    num=x
    sum=0
    while(num!=0):
        z=num%10
        num=num//10
        sum=sum+(z**2)
    return sum
ans=happy(x)


while(ans>9):
    ans=happy(ans)



  

if(ans==1):
    print('happy num')
elif(ans==4):
    print('unhappy number ')
