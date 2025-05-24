# This is a code for the Binary Search algorithm in Python

def binarySearch(array, requiredItem):
    low, high = 0, len(array)-1
    while low <= high:
        mid = (low + high) // 2
        midNumber = array[mid]
        print(f"Low : {low}, High : {high}, Mid : {mid}, Mid Number : {midNumber}")
        if midNumber == requiredItem:
            return mid
        elif midNumber > requiredItem:
            high = mid - 1
        elif midNumber < requiredItem:
            low = mid + 1
    return -1

if __name__ == '__main__':
    print(binarySearch([1, 2, 3, 4, 5, 6], 5))


