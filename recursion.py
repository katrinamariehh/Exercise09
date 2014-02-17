# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        popped = l.pop(0)
        return multiply_list(l) * popped

# Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

# Count the number of elements in the list l
def count_list(l):
    if list == []:
        return 0
    else:
        l.pop(0)
        return count_list(l) + 1

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        popped = l.pop(0)
        return sum_list(l) + popped

# Reverse a list without slicing or loops
def reverse(l):
    if l == []:
        return l
    else:
        popped = [l.pop(0)]
        return reverse(l) + popped

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

# Finds the item i in the list l.... RECURSIVELY
# Return the item if it is in the list or None if not found
def find(l, i):
    if l == []:
        return None
    elif l[-1] == i:
        return i
    else:
        l = l[0:-1]
        return find(l, i)

# Determines if a string is a palindrome
def palindrome(some_string):
    char_list = list(some_string)
    if len(char_list) == 1 or len(char_list) == 0:
        return True
    elif char_list[0] != char_list[-1]:
        return False
    char_list.pop()
    char_list.pop(-1)
    return palindrome(char_list)
    

# Given the width and height of a sheet of paper, and the number of times to fold it, 
# return the final dimensions of the sheet as a tuple. Assume that you always fold 
# in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    elif width > height:
        new_width = width/2
        num_folds = folds - 1
        return fold_paper(new_width, height, num_folds)
    elif height > width:
        new_height = height/2
        num_folds = folds - 1
        return fold_paper(width, new_height, num_folds)

# Count up
# Print all the numbers from 0 to target
# Use n to keep track of where you're at
# ex, to count from 1 - 100, call count_up(100, 1)
#
# Note: we don't have a test case for this one, so just run this
#       script directly
#
# Note #2: We're printing out the numbers, so this script does not 
#          need to return anything!
def count_up(target, n):
    return