
a = [8, 5, 2, 9, 5, 6, 3]

def bubbleSort(array):
    isSorted = False
    counter = 0
    print(array)
    while not isSorted:
        isSorted = True
        
        for i in range(len(array) - 1 ):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i+1], array[i]
                # swap(i, i + 1, array)
                isSorted = False
            print(f"------------------------ Counter : {counter}")
            print(array)
        counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

bubbleSort(a)