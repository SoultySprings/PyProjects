#The following code has a infinity recursion method also called as 'recurse' which means that it doesn't stop with time
#This error will pop up at most times when ran on a Python IDE

# Traceback (most recent call last):
#   File "C:\...\infinityRecursion.py", line 5, in infinity
#     infinity()
#   File "C:\...\infinityRecursion.py", line 5, in infinity
#     infinity()
#   File "C:\...\infinityRecursion.py", line 5, in infinity
#     infinity()
#   [Previous line repeated 997 more times]
# RecursionError: maximum recursion depth exceeded
def infinity():
    print('Recurse')
    infinity()

if __name__ == '__main__':
    infinity()
