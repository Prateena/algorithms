def swap(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k

def bubblesort_recursive(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            swap(A, i, i + 1)

    if n - 1 > 1:
        bubblesort_recursive(A, n - 1)

if __name__ == '__main__':
    
    A = [-3, -4, -5, 1, 7, 6, 4, 12, 0]

    bubblesort_recursive(A, len(A))

    print(A)