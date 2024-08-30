ele_input = input('Enter numbers separated by spaces: ')


elements = []
for i in ele_input.split():
    elements.append(int(i))


# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0  

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1  

    return comparisons, swaps

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0  
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1  
    return comparisons, swaps

# Insertion Sort Algorithm
def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0  
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1 
                j -= 1
            else:
                break
        
        if j + 1 != i:
            arr[j + 1] = key
            swaps += 1  

    return comparisons, swaps

# Shell Sort Algorithm
def shellSort(array):
    n = len(array)
    half = n // 2
    comparisons = 0
    swaps = 0  
    
    while half > 0:
        for i in range(half, n):
            var = array[i]
            j = i
            while j >= half and array[j - half] > var:
                comparisons += 1
                array[j] = array[j - half]
                j -= half
                swaps += 1 
            if j >= half:
                comparisons += 1
            array[j] = var
            if i != j:
                swaps += 1 
        half //= 2

    return comparisons, swaps

# Apply each sorting algorithm and print results


# Selection Sort
original_elements = elements.copy()
comparison_count, swap_count = selection_sort(original_elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array after selection sort:')
print(original_elements)
print(f'Number of comparisons: {comparison_count}')
print(f'Number of swaps: {swap_count}')



# Bubble Sort
original_elements = elements.copy()
comparison_count, swap_count = bubble_sort(original_elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array after bubble sort:')
print(original_elements)
print(f'Number of comparisons: {comparison_count}')
print(f'Number of swaps: {swap_count}')



# Insertion Sort
original_elements = elements.copy()
comparison_count, swap_count = insertion_sort(original_elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array after insertion sort:')
print(original_elements)
print(f'Number of comparisons: {comparison_count}')
print(f'Number of swaps: {swap_count}')




# Shell Sort
original_elements = elements.copy()
comparison_count, swap_count = shellSort(original_elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array after shell sort:')
print(original_elements)
print(f'Number of comparisons: {comparison_count}')
print(f'Number of swaps: {swap_count}')