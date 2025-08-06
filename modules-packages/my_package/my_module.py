

def greeting(): 
    print("Hello, this is greeting from my_module!")

def add_number(a,b): 
    return a + b     

# The __name__ variable demonstrates that if the file being run directly or imported as a module 

# This block of code will only run if the file is executed directly, not when imported
if __name__ == "__main__": 
    print("This is being run as a standalone program.")
    