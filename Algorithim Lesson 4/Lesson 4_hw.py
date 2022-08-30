#Even First Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
#Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(arr):
    pop_count = 0
    for i in range(0, len(arr)): #len = 8
        if arr[i - pop_count] % 2 == 1:
            arr.append(arr[i - pop_count])
            arr.pop(i - pop_count)
            pop_count += 1
    return arr
print(even_first([7, 3, 5, 6, 4, 10, 3, 2]))

#Increment a Number
#Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
#For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_number(arr):
    nine_count = 0
    for i in arr:
        if i == 9:
            nine_count += 1
    if nine_count == len(arr):
        for i in range(0, len(arr)):
            arr[i] = 0
        arr.insert(0, 1)
        return arr
    for i in range(-1, 0):
        if arr[i] == 9:
            arr[i] = 0
            if arr[i - 1] < 9:
                arr[i - 1] += 1
                return arr
        if arr[i] < 9:
            arr[i] += 1
            return arr
    return arr
print(increment_number([1, 2, 9]))