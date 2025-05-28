#This code has been taken from the book A CSG to DSA
#First converts all the readings from Fahrenheit to Celsius and then calculates the mean average of all the Celsius numbers
#The time complexity for the algorithm is 2N, but is taken as O(N)

import random as rd

def averageCelsius(fahrenheitReadings):
    if not fahrenheitReadings:
        return None

    celsiusReadings = []

    for fahrenheitReading in fahrenheitReadings:
        celsiusConversion = round(((fahrenheitReading - 32)/ 1.8), 3)
        celsiusReadings.append(celsiusConversion)

    sum = 0
    for celsiusReading in celsiusReadings:
        sum += celsiusReading

    return celsiusReadings, round((sum/len(celsiusReadings)), 3)

if __name__ == '__main__':
    array, i = [], 1
    while i<10:
        array.append(round(rd.uniform(32,212), 3))
        i+=1
    print(f'The readings in Fahrenheit are : {array}')
    resultArray, result = averageCelsius(array)
    print(f'The readings in Celsius are : {resultArray}, and the average is : {result}.')