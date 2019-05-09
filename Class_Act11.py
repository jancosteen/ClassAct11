num=15033377
p=0
convertNum = str(num)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
randomStrArr = []


def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    elif (n==0):
        return False
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True  

#Q1
for x in range(len(convertNum)):                
    if test_prime(int(convertNum[x])):
        p +=1

#Q2
import random
def Q2():
    return random.randint(25,51)

q=Q2()

#Q3
def Q3(q,p):
    return q%p

r= Q3(q,p)


randomNums=[]
#Q4
def Q4():
    length = 5
    randomString =""
    for x in range(r):
        if (length == 5):
            for z in range(5):
                randomString += alphabet[random.randint(0,25)]
            randomStrArr.append(randomString)    
            length = 7  
            randomString=""              
        elif (length == 7):
            for z in range(7):
                randomString += alphabet[random.randint(0,25)]
            randomStrArr.append(randomString)
            length = 5
            randomString=""
    return randomStrArr

print(Q4())  

    
