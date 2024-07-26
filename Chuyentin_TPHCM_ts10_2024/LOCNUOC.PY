n = 6
arr = [3, 4, 5, 6, 5, 1]




def is_mountain(arr):
    a_x = max(arr)
    print(a_x)
    arr_left = arr[:a_x]
    arr_right = arr[a_x:]
    
    print(arr)
    print(arr_left)
    print(arr_right)

is_mountain(arr)