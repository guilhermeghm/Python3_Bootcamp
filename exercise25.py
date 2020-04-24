##My solution
#Create a nested list

answer = [[num for num in range(0,10)] for val in range(0,10)]
print(answer)


##Offical solution
answer = [[i for i in range(0,10)] for num in range(0,10)]
