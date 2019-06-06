# def twoSum( nums, target):
#     output = []
#     for number in nums:
#         for i in range(nums.index(number)+1, len(nums)):
#             if number + nums[i] == target:
#                 output.append(nums.index(number))
#                 output.append(i)
#     return(output)
            
# nums = [2,7,11,15]
# target = (17)

# twoSum(nums, target)

for i in range(1,101):
    if i%3 ==0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)