import math

def mode(numbers):
    
    # Checking cases where list of numbers is 0,1, or 2
    if len(numbers) == 0:
        return None
    elif len(numbers) <= 2:
        return numbers[0]
    
    # Creating table with each number as the key and its count as the value
    hash_table = dict()
    for num in numbers:
        if num not in hash_table:
            hash_table[num] = 0
        hash_table[num] += 1
    
    # Finding the most frequent number
    mode = 0
    mode_count = 0
    for num in hash_table:
        current_count = hash_table[num]
        if current_count > mode_count:
            mode_count = current_count
            mode = num
    return mode



def main():
    # Testing
    arr = [3,3,4,3,1,3,1,3,3,4,5,5,5,5,5,5,5,5,7,7,89,9]
    print(mode(arr))

    """
    # Initial Testing
    arr = [3,3,4,3,1,3,1,3]
    tab = dict()
    for num in arr:
        if num not in tab:
            tab[num] = 0
        tab[num] += 1
    print(tab)
    """


if __name__ == '__main__':
    main()