





def dirReduc(arr):
    start = len(arr)
    print(start)
    for i in range(start-1):
        print(arr[i], arr[i+1])
        if arr[i] == "NORTH":
            if arr[i+1] != "WEST":
                arr.remove(arr[i])
        elif arr[i] == "WEST":
            if arr[i+1] != "SOUTH":
                arr.remove(arr[i])
        elif arr[i] == "SOUTH":
            if arr[i+1] != "EAST":
                arr.remove(arr[i])
        elif arr[i] == "EAST":
            if arr[i+1] != "NORTH":
                arr.remove(arr[i])
        # print(i)
    return arr

class A:
    def a(cls):
        return cls()

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))