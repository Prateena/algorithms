def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(a, start, end):

    pivot = a[end]

    sub_index = start

    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, sub_index)
            sub_index = sub_index + 1

    swap(a, end, sub_index)

    return sub_index

def QuickSort(a, start, end):

    if start >= end:
        return
    
    pivot = partition(a, start, end)

    QuickSort(a, start, pivot-1)

    QuickSort(a, pivot + 1, end)

if __name__ == '__main__':

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3, 0, -2]

    QuickSort(a, 0, len(a)-1)

    print(a)


