# Exception Handling Example

def Sum(n = input("Enter a number: ")):
    try:
        if 10/n == 0:
            print("The sum is zero.")
        else:
            print("The sum is not zero.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    finally:
        print("Execution completed.")

# Example usage

Sum(0)  # This will raise a ZeroDivisionError
Sum(5)  # This will not raise an error
        # print("Execution completed.")

# Manual Exception Raising Example

def Sum2(n = input("Enter a number: ")):
    raise ValueError("This is a custom error message.")

# Example usage for Else Block and Mutiple Exceptions

def square(n=input("Enter a number: ")):
    try:
        if n < 0:
            print("Negative value is not allowed.")
    except ValueError:
        print("Error: Negative value is not allowed.")
    except TypeError:
        print("Error: Invalid type. Please enter a number.")
    else:
        print(f"The square of {n} is {n**2}.")
    finally:    
        print("Execution completed.")

# Example usage for Multiple Exceptions together

def Sum3(n=input("Enter a number: ")):

    try:
        if n < 0:
            print("Negative value is not allowed.")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    else:
        print(f"The sum is {n + 10}.")
    finally:
        print("Execution completed.")
    
# Exception keywords like "zeroDivisionError", "ValueError", "TypeError" are called as Exception Classes.

# Custom Exception Example

class CustomError(Exception):
    pass

def raise_custom_error():
    try:
        raise CustomError("This is a custom error message.")
    except CustomError as e:
        print(f"Caught a custom error: {e}")
    finally:
        print("Custom error handling completed.")