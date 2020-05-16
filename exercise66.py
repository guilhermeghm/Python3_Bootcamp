#My solution
def max_magnitude(lst):
    lst = [abs(i) for i in lst]
    return max(lst)


#Official solution:
def max_magnitude(nums):
    return max(abs(num) for num in nums)


print(max_magnitude([300, 20, -900]))
