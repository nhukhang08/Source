def CSNT_BAI1(): # https://ucode.vn/problems/bai-1-liet-ke-cac-so-nguyen-to-trong-doan-lr-156140
    L, R = map(int, f.readline().split())
    def prime(x):
        if x in [2, 3]:
            return True
        elif x < 2 or x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x**0.5)+1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True
    arr = []
    for i in range(L, R+1):
        if prime(i):
            arr.append(i)
    g.write(str(len(arr))+ "\n")
    for i in range(len(arr)-1):
        g.write(str(arr[i])+ "\n")
    g.write(str(arr[-1]))

def CHUSO_BAI2():
    pass

def XAUCON_BAI3():
    pass

def SXPS_BAI4():
    pass

def NGTOFIB_BAI5():
    pass

def SO_BAI6():
    pass

def CHIAHET_BAI7():
    pass


def VITRISO_BAI8():
    pass

def GIAITHUA_BAI9():
    pass


f = open("input.txt", "r")
g = open("output.txt", "w")
def main():
    
    CSNT_BAI1()
    f.close(); g.close()

if __name__ == "__main__":
    main()