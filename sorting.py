ele_input = input('Enter numbers separated by spaces: ')


elements = []
for i in ele_input.split():
    elements.append(int(i))


#shellSort algorithm

def shellSort(array):
    n = len(array)
    half = n // 2
    comparisons = 0 
    
    while half > 0:
        for i in range(half, n):
            var = array[i]
            j = i
            while j >= half and array[j - half] > var:
                comparisons += 1 
                array[j] = array[j - half]
                j -= half
            if j >= half: 
                comparisons += 1
            array[j] = var
        half //= 2

    return comparisons 



print('The array before sorting is:')
print(elements)


comparison_count = shellSort(elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array in Ascending Order after shell sort:')
print(elements)
print(f'Number of comparisons: {comparison_count}')


# selection sort

def selection_sort(arr):
    n = len(arr)
    comparisons = 0  

  
    for i in range(n):
       
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1 
            if arr[j] < arr[min_idx]:
                min_idx = j
        
      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return comparisons



comparison_count = selection_sort(elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array in Ascending Order after selection sort: ')
print(elements)
print(f'Number of comparisons: {comparison_count}')


# bubble sort
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0  


    for i in range(n):
       
        for j in range(0, n - i - 1):
          
            comparisons += 1
          
            if arr[j] > arr[j + 1]:
               
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return comparisons




comparison_count = bubble_sort(elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array in Ascending Order after bubble sort: ')
print(elements)
print(f'Number of comparisons: {comparison_count}')


# insertion sort

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0  
    
 
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
       
        while j >= 0:
            comparisons += 1 
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        
        arr[j + 1] = key

    return comparisons




comparison_count = insertion_sort(elements)
print('---------------------------------------------------------------------------------------------------')
print('Sorted Array in Ascending Order after insertion sort: ')
print(elements)
print(f'Number of comparisons: {comparison_count}')

