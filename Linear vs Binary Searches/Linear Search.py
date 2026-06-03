def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        found += 1
        iterations = i + 1
    return -1

numbers = [5, 8, 12, 14, 19, 27, 33, 42]
target = int(input("Enter a number to search for: "))
result = linear_search(numbers, target)

if result != -1:
    print(f"Number found at index: {result}")
else:
    print("Number not found.")