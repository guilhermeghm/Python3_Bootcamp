##My solution
#Create a nested list as [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

answer = [[num for num in range(0,3)] for val in range(0,3)]
print(answer)


##Offical solution
answer = [[i for i in range(0,3)] for num in range(0,3)]
