print("whats is your name: ")
name=input()
print("which market did you go to: ")
market=input()
print("what did you buy: ")
food=input()
print("enter food amount: ")
amountfood=float(input())
print("what else did you buy: ")
food2=input()
print("enter your second food amount: ")
amoutfood2=float(input())
total=amountfood + amoutfood2
print("My purchase details are : " + name + " which market :" + market + ", what i bought: " + food + "," + str(amountfood) + "," +food2 + "," + str(amoutfood2)+ ",The total: " + str(total))