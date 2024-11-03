def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        if arr[mid] == target:
            return iterations, arr[mid]  # Якщо елемент знайдено, повертаємо його як верхню межу
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]  # Оновлюємо верхню межу
            right = mid - 1

    # Якщо елемент не знайдено, повертаємо верхню межу (найменший елемент, більший або рівний target)
    return iterations, upper_bound

# Приклад використання
arr = [0.1, 0.5, 1.2, 1.8, 3.3, 4.6, 5.9, 7.1]
target = 2.5
result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
