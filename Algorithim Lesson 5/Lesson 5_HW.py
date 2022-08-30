#Selection Sort Implement the selection sort algorithm that is sorting in descending order.
def selection_sort_desc(arr):
    for i in range(0, len(arr)):
        max_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

print(selection_sort_desc([5,34,5,4646,242,2425252,2324,1]))


#Bubble Sort Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort_desc(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return arr
print(bubble_sort_desc([3,5,42,443,4,2424,]))

#Insertion Sort Implement the insertion sort algorithm that is sorting in descending order.
def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort_desc([1,23,43,53,12,313,0]))
#Merge Sort Implement the merge sort algorithm that is sorting in descending order.
