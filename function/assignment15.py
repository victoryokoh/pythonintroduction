# group12.py

def fruits_operations():
    # Create a list of fruits
    fruits = ['apple', 'banana', 'orange', 'grape', 'mango']
    
    # Step 1: Print out the original list of fruits
    print("List of fruits:", fruits)

    # Step 2: Remove 'orange' from the list if it's there
    if 'orange' in fruits:
        fruits.remove('orange')
    
    # Print the final list of fruits after removing 'orange'
    print("Final list after removing orange:", fruits)

# Call the function to execute the code
fruits_operations()