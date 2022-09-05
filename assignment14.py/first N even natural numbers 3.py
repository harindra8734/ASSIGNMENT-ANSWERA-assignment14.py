#Write a Python script to create a list of first N even natural numbers
n=int(input("enter how many number you want to be store:"))
natural_number=[]
'''for i in range(1,n):
        i=i*2
        natural_number.append(i)
print(natural_number)'''

for i in range(1,n+1):

    i=i*2
    natural_number.append(i)
print(natural_number)