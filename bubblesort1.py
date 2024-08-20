def selection_sort(S):
    n = len(S)
    for i in range(n-1):
        min_ind = i
        for j in range(i+1, n):
            if S[min_ind]>S[j]:
                min_ind = j
        S[i], S[min_ind] = S[min_ind], S[i]

    print ("Selection Sorted Array is: ")
    for i in range(n):
        print(S[i],end=" ")

def bubblesort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False

        #last i elements are already in place
        for j in range(0, n-i-1):
            print(f"{i}th and {j}th pass {arr}")
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
                swapped = True
        print(f"{i}th and {j}th pass{arr}")
        if (swapped == False):
            break
    print(f"No. of changes {count}")




input_a = input("Enter elements of the list separated by space: ")
a = list(map(int, input_a.split()))

selection_sort(a.copy(),)
print()
print("---------------------------------------------")
bubblesort(a.copy())
        