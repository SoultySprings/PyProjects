#The following code has been taken from A CSG to DSA
#It calculates the sum from a low to high of a range using recurion

def sum(low, high):
    if high==low:
        return low
    else:
        return high + sum(low, high-1)

if __name__ == '__main__':
    low = 1
    high = 10
    print(f'The sum from {low} to {high} is {sum(low,high)}')