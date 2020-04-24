##My solution
#Numbers from 1 to 100 (including), only divisible by 12
answer = [num for num in range(1,101) if num %12 == 0]
print(answer)


##Official solution
answer = [val for val in range(1,101) if val % 12 == 0] 
