# You are given a list of unique integers arr, and two integers a and b. Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).




def consecutive(arr, a, b):
    x = 0

    while x < len(arr) - 1:
        if arr[x] == a and arr[x + 1] == b or arr[x] == b and arr[x + 1] == a:
            return True 
        x += 1
    return False 

print(consecutive([1, 3, 5, 7], 3, 7)) #, False
print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4)) #, True