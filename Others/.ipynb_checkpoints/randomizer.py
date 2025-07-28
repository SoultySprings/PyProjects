import random

def rnd():
    print("Hello")
    num,i = random.randrange(5,11,2),0
    numberOfEven, numberOfOdd = 0,0;
    while(i<num):

        i=i+1
    print(num)

if __name__ == '__main__':
    rnd()