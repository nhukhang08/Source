# m, n, k = map(int, input().split())
n = 3

def BHK(n):
    list_num = [2, 7]
    div = {}
    while list_num: 
        num = list_num.pop(0)
        if num % n == 0:
            return num
        if num%n not in div:
            div[num%n] = num
        print(div)

if __name__ == "__main__":
    BHK(n)
        
        
        
        