# Searching Problems and algorithm:

# Coded By: Sonu Shriram Vishwakarma (SE63)



# Create int list:

def createIntArr(size):

    array = []

    for i in range(size):

        element = int(input(f"Enter element No. {i+1}: "))

        array.append(element)

    return array



# Binary Search Using Recurssion

def binarySearch(key, array, low, high):

     

    if high>= low: # These codition is mainly used to check low should not greater than high because it cause list out of range error

        mid = (low + high)//2 # Floor division to ignoor flooting point number

      # mid = int((low + high)/2)

        if key == array[mid]:

            return mid

        elif key< array[mid]:

            return binarySearch(key, array, low, mid-1)

        else:

            return binarySearch(key, array, mid+1, high)

    else:

        return f"{key} Not Found"



# Linear Search 

def linearSearch(key, array):

    for i in range(len(array)):

        if key == array[i]:

            return i

    return f"{key} Not Found"



# Sentinal Search using recurssion

def sentinalSearch(array, key, lastIndex):

    if lastIndex >= 0:

        if key == array[lastIndex]:

            return lastIndex

        else:

            return sentinalSearch(array, key, lastIndex-1)

    else:

        return f"{key} Not Found"



# Fibonacci Search function

def fibonacciSearch(key, array):

    fibonacci = [0,1,1,2,3,5,8,13,21,34,55,89,144]

    n = len(array)

    for k in range(len(fibonacci)):

        if n <= fibonacci[k]:

            break

  

    if fibonacci[k]==0:

        return f"{key} Not Found"

    offset = -1

    

    while k>0:

        i = min(offset+fibonacci[k-2], n-1)

        

        if key == array[i]:

            return i

        elif key > array[i]:

            offset = i

        else:

            k = k-2

    return f"{key} Not Found"



size = int(input("Enter size of array or int(list): "))



array = createIntArr(size)



key = int(input("Enter which Roll No. you want to search: "))

low = 0

high = len(array)-1

index = binarySearch(key, array, low, high)

index1 = linearSearch(key, array)

index2 = sentinalSearch(array, key, high)

index3 = fibonacciSearch(key, array)



print(f"{key} Found at {index} using binary search")

print(f"{key} Found at {index1} using linear search")

print(f"{key} Found at {index2} using sentinal search")

print(f"{key} Found at {index3} using fibonacci search")

