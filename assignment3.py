first_number=int(input("please enter your first number: "))
second_number=int(input("please enter your second number: "))
third_number=int(input("please enter your third number: "))
sum=first_number+second_number+third_number
print("the sum of the numbers inputed  is",sum)
if sum>2000:
    print("sum is greater than 2000")
    sum2=sum*50
    print("the final total is",sum2)
else:
    print("the final total is",sum*3)
    print("the total is less than 2000")