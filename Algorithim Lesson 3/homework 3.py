
#Below The Arithmetical Mean
#When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
#The arithmetical mean is the sum of all elements divided by the number of elements.
#Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]

list = [1, 3, 5, 6, 4, 10, 2, 3]

 sum_number = sum(list)

length = len(list)

 arithmetical_mean = sum_number / length

 new_list = []

for num in list:
    if num < arithmetical_mean:
       new_list.append(num)

 print(new_list)

def list_below_arithmetical_mean(list):  #o(n)
    sum_list = sum(list)
    length_list = len(list)
    arithmetical_mean = sum_list / length_list
    new_list = []
    for num in list:
        if num < arithmetical_mean:
            new_list.append(num)
    return new_list

list = [1, 3, 5, 6, 4, 10, 2, 3]
print(list_below_arithmetical_mean(list))

#Two Lowest Elements
#When given a list of elements, find the two lowest elements.
#They can be equal to each other or different.
#Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


#method1     O(logn)


def lowest_elements(list):
    list1 = sorted(list)
    min1, min2 = list1[0:2]
    return min1, min2


list = [198, 3, 4, 9, 10, 9, 2]
print(lowest_elements(list))