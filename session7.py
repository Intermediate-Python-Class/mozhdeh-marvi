my_array = [1, 2, 3, 4, 6, 5, 8, 9, 10]

def find_missing_values(nums): 
    n = len(nums) + 1
    total = n * (n+1) // 2

    actual = sum(nums)
    return total - actual

missing_num = find_missing_values(my_array)

print('the missing value is:' , missing_num)