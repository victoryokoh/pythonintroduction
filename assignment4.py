first_number=int(input("please enter your first number: "))
second_number=int(input("please enter your second number: "))
third_number=int(input("please enter your third number: "))
fourth_number=int(input("please enter your fourth number: "))
sum=first_number+second_number+third_number+fourth_number
print("the sum of the numbers inputed  is",sum)
if sum<4000:
    print("sum is less than 4000")
    sum2=sum/4
    print("the final result is",sum2)
else:
    print("the final total is",sum-200)
    print("the total is greater than 4000")