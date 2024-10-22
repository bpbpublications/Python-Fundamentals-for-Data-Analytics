# defining a variable in the module
var1 = 10
var2 = 'Computer'

# defining a function in the module
def oddeven( number ):          # this function is used to find if a number is even or odd
    if (number % 2 == 0):
        result = 'Even'
    else:
        result = 'Odd'
    return result    # here, we are returning the result of the function

if __name__ == "__main__":
    # some python statements
    print("Hello, Welcome to module2!")
    print("Thank you for your interest in the module.")