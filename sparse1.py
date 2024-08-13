# n = int(input("Enter the no of rows: "))
# m = int(input("Enter the no of cols: "))
# sparse = []
# sparse2= []
# count2 = 0
count = 0
# for i in range(0,n):
#     for j in range(0,m):
#         a = int(input(f"Enter {i},{j} element: "))
#         if a!=0:
#             sparse.append([i,j,a])
#             count+=1
# sparse = [[n,m,count]] + sparse
sparse = [[3,3,4],[0,0,1],[1,2,2],[2,0,2],[2,1,1]]
for i in sparse:
    print(i)

print()
# n2 = int(input("Enter the no of rows: "))
# m2 = int(input("Enter the no of cols: "))
# for i in range(0,n2):
#     for j in range(0,m2):
#         a = int(input(f"Enter {i},{j} element: "))
#         if a!=0:
#             sparse2.append([i,j,a])
#             count2+=1
# sparse2 = [[n2,m2,count2]] + sparse2
# for i in sparse:
#     print(i)

def transpose(mat,n,m):
    for i in mat:
        a = i[0]
        i[0]=i[1]
        i[1]=a
    mat = [[n,m,count]]+sorted(mat[1:])
    return mat

# for i in transpose(sparse):
#     print(i)

def simpleTrans(mat):
    transMat = [] + mat[:1]
    for i in range(0,mat[0][1]):
        for j in range(1,mat[0][2]+1):
            if mat[j][1]==i:
                transMat.append([mat[j][1],mat[j][0],mat[j][2]])
    return transMat



# print(sparse)
# print(sparse2)

# def addition(mat,mat2):
#     addMat = []
#     if(mat[0][0]==mat2[0][0] and mat[0][1]==mat2[0][1]):
#         c1 = c2 = 1
#         while(c1<mat[0][2] and c2<mat2[0][2]):
#             if mat[c1][1]==mat[c2][1] and mat[c1][0]==mat2[c2][0]:
#                 addMat.append([mat[c1][0],mat[c1][1],mat[c1][2]+mat2[c2][2]])
#                 c1+=1
#                 c2+=1
#             elif mat[c1][0]==mat2[c1][0]:
#                 if mat[c1][1]<mat2[c2][1]:
#                     addMat.append([mat[c1][0],mat[c1][1],mat[c1][2]])
#                     c1+=1
#                 elif mat[c1][1]>mat2[c2][1]:
#                     addMat.append([mat2[c2][0],mat2[c2][1],mat2[c2][2]])
#                     c2+=1
#             elif mat[c1][1]==mat2[c1][1]:
#                 if mat[c1][0]<mat2[c2][0]:
#                     addMat.append([mat[c1][0],mat[c1][1],mat[c1][2]])
#                     c1+=1
#                 elif mat[c1][0]>mat2[c2][0]:
#                     addMat.append([mat2[c2][0],mat2[c2][1],mat2[c2][2]])
#                     c2+=1
#         while(c1<mat[0][2]):
#             addMat.append([mat[c1][0],mat[c1][1],mat[c1][2]])
#         while(c2<mat2[0][2]):
#             addMat.append([mat2[c2][0],mat2[c2][1],mat2[c2][2]])

#         for i in addMat:
#             print(i)
#     else:
#         print("Operation Not Possible")


for i in simpleTrans(sparse):
    print(i)

def fastTranspose(sp1):
    sp2 = [[sp1[0][1],sp1[0][0],sp1[0][2]]] + [0]* sp1[0][2]
    print(sp2)
    freq = [0] * (sp1[0][1]+1)
    for i in sp1[1:]:
        freq[(i[1])+1] += 1
    print(freq)
    freq[0]=1
    for i in range(1,len(freq)-1):
        freq[i] = freq[i-1]+freq[i]
    print (freq)
    print()
    for i in sp1[1:]:
        sp2[freq[i[1]]] = [i[1],i[0],i[2]]
        freq[i[1]]+=1
    for i in sp2:
        print(i)


print("-------------------------------------------------------------------------")

def addition(mat, mat2):
    addMat = []
    i, j = 0, 0
    
    while i < len(mat) and j < len(mat2):
        if mat[i][0] == mat2[j][0] and mat[i][1] == mat2[j][1]:
            # Both entries have the same row and column
            addMat.append([mat[i][0], mat[i][1], mat[i][2] + mat2[j][2]])
            i += 1
            j += 1
        elif (mat[i][0] < mat2[j][0]) or (mat[i][0] == mat2[j][0] and mat[i][1] < mat2[j][1]):
            # mat1 entry is smaller
            addMat.append([mat[i][0], mat[i][1], mat[i][2]])
            i += 1
        else:
            # mat2 entry is smaller
            addMat.append([mat2[j][0], mat2[j][1], mat2[j][2]])
            j += 1
    
    # Add remaining elements from mat1
    while i < len(mat):
        addMat.append([mat[i][0], mat[i][1], mat[i][2]])
        i += 1
    
    # Add remaining elements from mat2
    while j < len(mat2):
        addMat.append([mat2[j][0], mat2[j][1], mat2[j][2]])
        j += 1
    
    return addMat
mat= [
    [0, 0, 1],
    [0, 1, 2],
    [1, 0, 3]
]

mat2 = [
    [0, 0, 4],
    [0, 1, 5],
    [1, 1, 6]
]

result = addition(mat, mat2)
print(result)
