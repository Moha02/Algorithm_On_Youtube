


a = [7, 9, 5, 4, 2, 9 , 3, 4]


def insertion_sort(array):

    counter = 0

    for x in range(1, len(array)):

        while array[x - 1] > array[x] and x > 0:

            swap(x, array)
            print(array)


            x -= 1
        print("Out of while loop")
        # print(array)

        print(f"------------------- {counter}")
        counter += 1



def swap(i , array):
    array[i - 1], array[i] = array[i], array[i - 1]


insertion_sort(a)


