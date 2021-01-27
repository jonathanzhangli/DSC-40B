import math

def logcount(arr, a, b): 
  
    # Check base case 
    if len(arr) == 0:
        return 0
    middle = math.floor(len(arr)/2)
    if arr[middle] > b:
        # print('greater' + str(arr))
        return logcount(arr[:middle], a, b)
    elif arr[middle] < a:
        # print('less' + str(arr))
        return logcount(arr[middle + 1:], a, b)
    else:
        # print('equal' + str(arr))
        return 1 + logcount(arr[:middle], a, b) + logcount(arr[middle + 1:], a, b)



def main():
    # Testing
    arr = [2, 3, 5, 5, 6, 9, 12]
    arr1 = [10]
    arr2 = [5,5,5,5,5]
    a = 3.7
    b = 6.1
    print(logcount(arr2, a, b))


if __name__ == '__main__':
    main()