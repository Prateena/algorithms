def binarySearch(nums, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if target == nums[mid]:
        return mid
    elif target <= nums[mid]:
        return binarySearch(nums, left, mid - 1, target)
    else:
        return binarySearch(nums, mid + 1, right, target)

if __name__ == '__main__':

    nums = [2, 4, 6, 8, 9, 10]
    target = 10

    left, right = 0, len(nums) - 1

    index = binarySearch(nums, left, right, target)  

    if index != -1:
        print("Element Found at index", index)
    else:
        print("Element not Found")