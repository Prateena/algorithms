def Left(i):
    return 2 * i + 1

def Right(i):
    return 2 * i + 2

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def heapify(A, i, size):

    left = Left(i)
    right = Right(i)

    largest = i

    if left < size and A[left] > A[i]:
        largest = left

    if right < size and A[right] > A[largest]:
        largest = right

    if largest != i:
        swap(A, i, largest)
        heapify(A, largest, size)

def pop(A, size):

    if size <= 0:
        return -1
     
    top = A[0]

    A[0] = A[size - 1]

    heapify(A, 0, size - 1)

    return top

def heapsort(A):

    n = len(A)

    i = (n - 2) // 2
    
    while i >= 0:
        heapify(A, i, n)
        i = i - 1

    while n:
        A[n - 1] = pop(A, n)
        n = n - 1

if __name__ == '__main__':

    A = [-3, 2, 1, 0, 10, 11, 9, 8]

    heapsort(A)

    print(A)

