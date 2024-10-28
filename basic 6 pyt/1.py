def binary_search(arr, target):
    def search(left, right):
        if left > right:
            return -1  
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  
        return search(mid + 1, right) if arr[mid] < target else search(left, mid - 1)

    return search(0, len(arr) - 1)

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

position = binary_search(sorted_list, target_value)

if position != -1:
    print(f"Элемент {target_value} найден на позиции {position}.")
else:
    print(f"Элемент {target_value} не найден в списке.")