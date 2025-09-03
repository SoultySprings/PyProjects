import random, seaborn as sns
import matplotlib.pyplot as plt

def rnd(choice, numberOfRepetitions):
    j=0
    numDict  = {"numberOfEven":0, "numberOfOdd" :0}
    while(j<numberOfRepetitions):
        i=0
        numberOfEven, numberOfOdd = 0, 0
        while(i<choice):
            num2 = random.randint(1,20)
            if(num2%2==0):
                numberOfEven+=1
            else:
                numberOfOdd+=1
            i+=1
        numDict["numberOfEven"] = numberOfEven
        numDict["numberOfOdd"] = numberOfOdd
        print(f"Number of choices : {choice} \nNumber of Even numbers : {numDict["numberOfEven"]} and \nNumber of Odd numbers : {numDict["numberOfOdd"]}")
        print("Winner is Even!") if numberOfEven>numberOfOdd else print("Winner is Odd!")
        print("\n")
        j+=1
        fig = sns.barplot(data=numDict)
        plt.show()

if __name__ == '__main__':
    # choice = int(input("Hey there! Random choice generator based on numbers! Mention the number of choices please : "))
    # number_of_time = int(input("Mention the number of times it should be repeated please : "))
    # if(choice%2==1 and number_of_time%2==1):
    print("Okay lets randomize this and tell you:")
    rnd(9999, 9)
    # else:
    #     print("Okay lets randomize this and tell you ")