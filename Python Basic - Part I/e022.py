def list_count_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count

print(list_count_4([1,4,6,1,3,6,7,24,2,3,4,3,3,5,5,5,4,]))