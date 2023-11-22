def swap(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k

def selectionsort(A):
    for i in range(len(A)-1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j

        swap(A, min, i)

if __name__ == '__main__':

    A = [3, 2, 6, 9, 10, -1, 0, 8]

    selectionsort(A)

    print(A)