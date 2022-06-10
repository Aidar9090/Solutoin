def twoSum(nums, target):
    check ={}
    for i in range(len(nums)):
        if target - nums[i] in check:
            return [i, check[target-nums[i]]]
        else:
            check[nums[i]]=i

print(twoSum([2,7,11,15], 9))

# def isPalindrome(x: int) -> bool:
#     a = str(x)
#     if a == a[::-1]:
#         return True
#     else: 
#         print(False)
#     p = int(x)

# print(isPalindrome(353))

# def say_hello(name, city, state):
#     x = " ".join(name)
#     return f"Hello, {" ".join(x)}! Welcome to {city}, {state}"
