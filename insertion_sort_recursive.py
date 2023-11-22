def insertionSort(A, i, n):
    value = A[i]
    j = i

    while j > 0 and A[j - 1] >  value:
        A[j] = A[j - 1]
        j = j - 1

    A[j] = value

    while i + 1 <= n:
        insertionSort(A, i + 1, n) 

if __name__ == '__main__':

    A = [-9, -10, -2, 1, 0, 9, 7, 4, 3, 11]

    insertionSort(A, 1, len(A) - 1)

    print(A)