# word="monument"
# for char in word:
#     print(char) 


#activity 2
# number=int(input("enter the no. for tables:"))
# for i in range(1,11):
#     print(number,"x",i,"=",number*i)

#activity 3
# number=sum(range(1,3098))
# print(number)

#activity 4
number=int(input("enter the no. to check prime or not:"))
flag=False
if number>1:
    for i in range(2,number):
        if(number%i==0):
            flag=True
            break

if flag:
    print("number is not prime",number)
else:
    print("number is prime",number)        



