def check_product():
    numbers = [24, 46, 102]
    
    # Multiply all the numbers
    product = 1
    for num in numbers:
        product *= num
    
    # Check if the product is equal to 144
    if product == 144:
        print("Hurray! It is equal to 144")
    else:
        print("Oh no! It is not equal to 144")

if __name__ == "__main__":
    check_product()