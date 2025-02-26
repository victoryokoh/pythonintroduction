def manipulate_numbers():
    numbers = [1, 13, 30, 50, 35, 16, 80, 19]
    
    # i. Print the list out
    print("List of numbers:")
    print(numbers)
    
    # ii. Print the sum out
    total = sum(numbers)
    print("Sum of the list:")
    print(total)
    
    # iii. Check if the sum is greater than 100
    if total > 100:
        print("It is greater than 100")
    else:
        print("It is less than 100")

if __name__ == "__main__":
    manipulate_numbers()