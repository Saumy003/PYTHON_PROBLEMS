# SORTING ALGO #

# 1. BUBBLE SORT
nums = [ 5, 2, 9, 7, 1, 3, 6]
n = len(nums)

for i in range(n-2, -1, -1):
    for j in range(0, i+1):
        if nums[j]> nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

print("Sorted array:",nums)

#2. Selection Sort
