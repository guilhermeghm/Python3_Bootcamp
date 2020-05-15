'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

#My solution
def list_manipulation(list,command,location,value=0):
    if command == "remove":
        if location == "end":
            return list.pop(-1)
        else:
            return list.pop(0)
    if command == "add":
        if location == "end":
            list.append(value)
            return list
        else:
            list.insert(0,value)
            return list

#Official solution
def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
