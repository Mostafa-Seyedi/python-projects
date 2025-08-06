# Error Handling Example

# Function to divide two numbers with proper error handling
def divide(a, b):
    try:
        # Attempt to divide the numbers
        result = a / b
    except ZeroDivisionError:
        # Handle the case where b is 0
        print("Error: Division by zero is not allowed!")
        return None
    except TypeError:
        # Handle the case where the input types are not valid for division
        print("Error: Both inputs must be numbers!")
        return None
    else:
        # This block executes if no error occurred in the try block
        print(f"The result is: {result}")
        return result
    finally:
        # This block always runs, regardless of errors
        print("Execution completed!")

# Example usage
print("Test 1:")
divide(10, 2)  # Normal division

print("\nTest 2:")
divide(10, 0)  # Division by zero

print("\nTest 3:")
divide(10, "a")  # Invalid input type (TypeError)
