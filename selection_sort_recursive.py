def swap(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k

def selectionsortRecursive(A, i, n):

    min = i

    for j in range(i + 1, n):
        
        if A[j] < A[min]:
            min = j

    swap(A, min, i)

    if i + 1 < n:
        selectionsortRecursive(A, i+1, n)

if __name__ == '__main__':

    A = [-2, -9, -1, 9, 7, 12, 0]

    selectionsortRecursive(A, 0, len(A))

    print(A)
