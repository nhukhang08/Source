# m, n, k = map(int, input().split())
n = 3

def BHK(n):
    list_num = [2, 7]
    # 
    div = {}
    while list_num: 
        num = list_num.pop(0)
        if num % n == 0:
            return num
        if num%n in div:
            for num in "027":
                list_num.append( int ( str(list_num[0]) + num ) % n )
                if int ( str(list_num[0]) + num ) % n == 0:
                    return int ( str(list_num[0]) + num )
        else:
            div[num%n] = num


print(BHK(n))