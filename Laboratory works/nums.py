from random import randint

n = int(input())
nums = [randint(1, n) for i in range(1, n + 1)]
nums_normal_distribution = [i for i in range(1, n + 1)]

def find_missing_numbers():
    print(nums)
    print(nums_normal_distribution)
    missing_numbers = [i for i in nums_normal_distribution if i not in nums]
    print(missing_numbers)
    
find_missing_numbers()
