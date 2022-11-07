

a = [9, 6, 2, 4, 8]

def SelectionSort(array):

    for x in range(len(array)):

        midIndex = x
        print("----------------")
        print(array)
        print(f" x : {x}, the pointer at {array[x]}")

        for j in range( x + 1, len(array)):
            print(f" j : {j}, the pointer is compared to {array[j]}")

            if array[j] < array[midIndex]:

                midIndex = j
                print(f" mid point : {array[midIndex]}")

        array[x], array[midIndex] = array[midIndex], array[x]
        print(f" Swap {array[x]} with {array[midIndex]} ")
SelectionSort(a)