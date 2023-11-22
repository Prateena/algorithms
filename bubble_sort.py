def swap(A, i, j):
    k = A[i]
    A[i] = A[j]
    A[j] = k

def bubblesort(A):
    for k in range(len(A) - 1):
        for i in range(len(A) - 1 - k):
            if A[i] > A[i + 1]:
                swap(A, i, i + 1)
        
if __name__ == "__main__":

    A = [-9, -10, 9, 8, 5, 0, 1, 4]

    bubblesort(A)

    print(A)

