def input_sparse_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    sparse_matrix = []
    count = 0
    for i in range(rows):
        for j in range(cols):
            value = int(input(f"Enter element at ({i},{j}): "))
            if value != 0:
                sparse_matrix.append([i, j, value])
                count += 1
    return [[rows, cols, count]] + sparse_matrix

def simple_transpose(matrix):
    rows, cols, _ = matrix[0]
    transpose_matrix = [[cols, rows, matrix[0][2]]]
    for col in range(cols):
        for element in matrix[1:]:
            if element[1] == col:
                transpose_matrix.append([element[1], element[0], element[2]])
    return transpose_matrix

def add_sparse_matrices(mat1, mat2):
    result = []
    i, j = 1, 1
    while i < len(mat1) and j < len(mat2):
        if mat1[i][:2] == mat2[j][:2]:
            result.append([mat1[i][0], mat1[i][1], mat1[i][2] + mat2[j][2]])
            i += 1
            j += 1
        elif mat1[i][:2] < mat2[j][:2]:
            result.append(mat1[i])
            i += 1
        else:
            result.append(mat2[j])
            j += 1
    result.extend(mat1[i:])
    result.extend(mat2[j:])
    return [[mat1[0][0], mat1[0][1], len(result) - 1]] + result

def fast_transpose(matrix):
    rows, cols, count = matrix[0]
    transpose_matrix = [[cols, rows, count]]
    freq = [0] * (cols + 1)
    
    for element in matrix[1:]:
        freq[element[1] + 1] += 1
    
    freq[0] = 1
    for i in range(1, len(freq) - 1):
        freq[i] += freq[i - 1]
    
    temp_matrix = [None] * (count + 1)
    for element in matrix[1:]:
        temp_matrix[freq[element[1]]] = [element[1], element[0], element[2]]
        freq[element[1]] += 1
    
    transpose_matrix.extend(temp_matrix[1:])
    return transpose_matrix

def main():
    menu = """
    Choose from the options:
    1. Add matrices
    2. Simple transpose
    3. Fast transpose
    """
    print(menu)
    option = int(input("Enter the option (1/2/3): "))

    sparse_matrix1 = input_sparse_matrix()
    
    if option == 1:
        sparse_matrix2 = input_sparse_matrix()
        result = add_sparse_matrices(sparse_matrix1, sparse_matrix2)
        print("Result of addition:")
        for row in result:
            print(row)
    elif option == 2:
        result = simple_transpose(sparse_matrix1)
        print("Result of simple transpose:")
        for row in result:
            print(row)
    elif option == 3:
        result = fast_transpose(sparse_matrix1)
        print("Result of fast transpose:")
        for row in result:
            print(row)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()