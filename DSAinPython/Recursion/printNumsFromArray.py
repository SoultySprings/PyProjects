#The following code has been taken from A CSG to DSA
#It prints only numbers from a combination of arrays and numbers using recurion


def printAllNumbers(array):
    for value in array:
        if isinstance(value, list):
            printAllNumbers(value)
        else:
            print(f'{value}', end=', ')

if __name__ == '__main__':
    array = [
        1,
        2,
        3,
        [4, 5, 6],
        7,
        [8,
         [9, 10, 11,
          [12, 13, 14]
          ]
         ],
        [15, 16, 17, 18, 19,
         [20, 21, 22,
          [23, 24, 25,
           [26, 27, 29]
           ], 30, 31
          ], 32], 33
    ]

    print(f'The array is {array} and result is ')
    printAllNumbers(array)
