num=15033377
p=0
convertNum = str(num)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
randomStrArr = []
vowels="aeoiu"

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

print("1. Number of prime numbers:")
print(p)

#Q2
import random
def Q2():
    return random.randint(25,51)

q=Q2()
print("2. The random number is:")
print(q)

#Q3
def Q3(q,p):
    return q%p

r= Q3(q,p)
print("3. The number of strings to be generated is: ")
print(r)

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

   
randomStrArr=Q4()
print("4.List of strings: ")
print(randomStrArr)

#Q5
def vowel_Counter(array):    
    string=""
    vowel_countArr=[]
    for x in range(len(array)):
        string=array[x]
        count=0
        for s in string:            
            if s in vowels: count+=1
        vowel_countArr.append(count)
    return vowel_countArr

vowel_countArr=vowel_Counter(randomStrArr)
print(vowel_countArr)

def Q5(stringArray,vowelCountArray):
    vowel_dict ={}
    for x in range(len(stringArray)):
        vowel_dict[stringArray[x]] = "(Vowels: "+str(vowel_countArr[x])+")"
    return vowel_dict

def q5(stringArray, vowel_countArr):
    ordered_list=[]
    for x in range(len(stringArray)):
        ordered_list.append(str(stringArray[x]+" (Vowels: "+ str(vowel_countArr[x])+")"))
    return ordered_list

ordered_list = q5(randomStrArr,vowel_countArr)
final_dict = Q5(randomStrArr,vowel_countArr)
print("5. Sorted list of strings: ")
print(ordered_list)