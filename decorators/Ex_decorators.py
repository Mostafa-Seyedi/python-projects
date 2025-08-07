

"""
What are decorators?
--------------------
Decorators are special functions in Python that allow you to add extra 
functionality to other functions without changing their actual code. 
They "wrap" another function to extend or modify its behavior.

In this example, we use a decorator called `run_on_even_minute` that only 
allows the decorated function to run if the current minute is even. 
Otherwise, it prints a message asking the user to wait.

This is useful when you want to apply the same logic (like logging, access control, 
or timing) to multiple functions in a clean and reusable way.

"""

import datetime

# Decorator that only allows function execution if the current minute is even
def run_on_even_minute(func): 
    def wrapper(): 
        now = datetime.datetime.now()
        minute = now.minute
        if minute % 2 == 0:
            func()
        else: 
             print("⚠️ Shhh... It's an odd minute. Come back later.")
        
    return wrapper    


# Using the decorator on different functions
@run_on_even_minute
def great(): 
    print("👋 Hello there!")

@run_on_even_minute
def farewell(): 
    print("👋 Goodbye!")


# Testing the decorated functions
great()
farewell()