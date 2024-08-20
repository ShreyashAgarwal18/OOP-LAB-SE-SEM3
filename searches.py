a=[]


def linearSearch(lst,ele):
    ret=-1
    count=0
    for i in range(len(lst)):
        count+=1
        if lst[i]==ele:
            ret=i
            break
    return ret,count


def binarySearch(lst,s,e,ele,count = 0):
    if s>e:
        return (-1,count)
    else:
        s=s
        e=e
        m=int((s+e)/2)
        if lst[m]==ele:
            return (m,count)
        elif ele>lst[m]:
            return binarySearch(lst,m+1,e,ele,count+1)
        elif ele<lst[m]:
            return binarySearch(lst,s,m-1,ele,count+1)


def binarySearch2(lst,ele):
    s=0
    e=len(lst)-1
    while(s<e):
        m=(s+e)//2
        if lst[m]==ele:
            return m
        elif ele>lst[m]:
            s=m+1
        elif ele<lst[m]:
            e=m-1
    pass

def sentinalSearch(lst,ele):
    lst2 = lst.copy()
    lst2.append(ele)
    i=0
    count = 0
    while lst2[i]!=ele:
        i+=1
        count+=1
    if i<len(lst2)-1:
        return i,count
    else:
        return -1,count
    

def fibonacciSearch(arr,ele):
    count = 0
    offset = 0
    fibm = 1
    fibm1 = 0
    fibm2 = 0
    while fibm < len(arr):
        fibm2 = fibm1
        fibm1 = fibm
        fibm = fibm1 + fibm2
    while fibm > 1:
        i = min(offset + fibm2, len(arr)-1)
        if arr[i] < ele:
            fibm = fibm1
            fibm1 = fibm2
            fibm2 = fibm - fibm1
            offset = i
            count += 1
        elif arr[i] > ele:
            fibm = fibm2
            fibm1 = fibm1 - fibm2
            fibm2 = fibm - fibm1
            count += 1
        elif arr[i] == ele:
            return i,count
    return -1,count


input_str_a = input("Enter elements the list: ")
a = input_str_a.split()  
a = sorted([int(num) for num in a])
ele=int(input("Enter the element to search: "))


def binaryCheck():
    print()
    print("Using Binary Search")
    ans = binarySearch(a,0,len(a),ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
        
    else:
        print("Element found at", ans[0])
        print("The no of comparisions:",ans[1])

def linearCheck():
    print()
    print()
    print("Using linear search")
    ans = linearSearch(a,ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"Element found at", ans[0])
        print("The no of comparisions:",ans[1])

def sentinalCheck():
    print()
    print()
    print("Using sentinal search")
    ans = sentinalSearch(a,ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"Element found at", ans[0])
        print("The no of comparisions:",ans[1])

def fibonacciCheck():
    print()
    print()
    print("Using fibonacci search")
    ans = fibonacciSearch(a,ele)
    if ans[0]<0:
        print("Element not found")
        print("The no of comparisions:",ans[1])
    else:
        print(f"Element found at", ans[0])
        print("The no of comparisions:",ans[1])


linearCheck()
sentinalCheck()
binaryCheck()
fibonacciCheck()