def InsertionSort(A):
    for i in range(1, len(A)):

        value = A[i]
        j = i

        while j > 0 and A[j - 1] > value:
            A[j] = A[j - 1]
            j = j - 1

        A[j] = value

if __name__ == "__main__":

    A = [3, 2, -2, -3, 0, 1, 5, 9, 8, 12]

    InsertionSort(A)

    print(A)


    

