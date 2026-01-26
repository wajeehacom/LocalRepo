def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
numbers_list = [2, 7, 11, 15]
target_value = 9
print("Hello from feature1 branch")
print("sum of two target Element:",two_sum(numbers_list,target_value))