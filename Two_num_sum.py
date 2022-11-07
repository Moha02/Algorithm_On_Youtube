

def twoNumSum(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        sum = array[left] + array[right]
        print(f"The sum of two numbers is :{sum} sums of {array[right]} and {array[left]}")
        # print(f"The right index : {right} and The left index : {left}")
        
        if sum < target:
            
            print("The left pointer has moved to the right")
            print(f"The left index : {left}")

            left += 1

        elif sum > target:
            
            print("The right poninter has moved to the left")
            print(f"The right index : {right}")
            right -= 1

        elif sum == target:

            print(f"found the two integers {array[left]} and {array[right]}")
            return [array[left], array[right]]

    return []


a = [-2, 4, 5, -3, 8, 4, 2,-4,9]
print(f"The length of the list is {len(a)}")
a.sort()
print(a)

twoNumSum(a, 100)