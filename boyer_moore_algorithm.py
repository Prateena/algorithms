def findmajorityelements(nums):
    count = 1
    
    highest_repitition = []
    highest_repitition_item = 0

    for i in nums:
        if i in highest_repitition:
            highest_repitition_item = i
            count += 1
        else:
            highest_repitition.append(i)
    print("The majority element is {} which occurs {} times in the list".format(highest_repitition_item, count))

nums=[2,3,4,2,2]
findmajorityelements(nums)