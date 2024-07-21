f = open("input.txt", "r")
g = open("output.txt", "w")

def CSNT_BAI1():
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
        g.write(str(arr[i])+ " ")

    g.write(str(arr[-1]))


def CHUSO_BAI2():
    m, n, k = map(int, f.readline().split())

    t = "1"
    for i in range(n):   
        if len(t) < k:
            t = str(int(t) * m)
        else:
            t = str(int(t[len(t)-k:]) * m)

    result = str(t[len(t)-k:])

    if len(result) < k:
        result = "0" * ( k - len(result) ) + result

    g.write(result)

def XAUCON_BAI3():
    s = str(f.readline())

    arr = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            ch = s[i:j]
            if ch not in arr:
                arr.append(ch)

    g.write(f"{len(arr)}")



def string():
    k = int(f.readline())
    char = f.readline()
    result = []
    for i in range(len(char)):
        result.append(char[(k + i) % len(char)])

    result = "".join(result)

    g.write(str(result))

def SXPS_BAI4():
    n, k = map(int, f.readline().split())

    phanso = []
    dec = []
    for i in range(n+1):
        for j in range(i+1, n+1):
            if i/j not in dec:
                phanso.append(f"{i}/{j}")
                dec.append(i/j)


    def sapxep(arr: int, lst: str):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    result = sapxep(dec, phanso)
    g.write(result[k-1])

def NGTOFIB_BAI5():
    """
    Input: int N
    Output: Là số X và những số thay đổi vị trí của X thõa mãn điều kiện
    Ý tưởng: 
        Duyệt các số fib thứ tự từ 7 đến x sao cho fib[i] <= N
            Kiểm tra số nguyên tố
                Tạo hoán vị cho số
                    Kiểm tra số nguyên tố
                    {
                        Lưu kết quả
                    }
        In kết quả

    """    
    MOD = 10000000000
    def matrix_mul(a, b):
        arr = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    arr[i][j] += a[i][k] * b[k][j]
                    arr[i][j] %= MOD
        return arr

    def matrix_root(a): return matrix_mul(a, a)

    def binpow(a, n):
        if n == 1:
            return a
        tmp = binpow(a, n // 2)
        if n % 2 == 1:
            return matrix_mul(matrix_root(tmp), a)
        else:
            return matrix_root(tmp)

    fib = [[1, 1], [1, 0]]

    def is_prime(x):
        if x in [2, 3]:
            return True
        if x < 2 or x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x**0.5)+1, 6):
            if x % i == 0 or x % (i+2) == 0:
                return False
        return True


    def hoanvi(x):
        x = str(x)
        result = []
        def backtrack(path, options):
            if len(options) == 0:
                number = int(path)
                if is_prime(number) and number not in result:
                    result.append(number)
                return
            if len(result) == 2:
                return

            for i in range(len(options)):
                backtrack(path + options[i], options[:i] + options[i+1:])
        backtrack("", x)

        return result


    n = int(f.readline())

    num = 0
    index = 7
    result = []
    while num < n:
        num = binpow(fib, index)[0][1] # Fib
        if num > n:
            break
        index += 1
        # -----------------------
        if is_prime(num) and len(hoanvi(num)) == 2:
            nums = hoanvi(num)
            
            result.append(nums)

    for i in range(len(result)-1):
        for j in range(1):
            g.write(str(result[i][j]) + " ")
        g.write(str(result[i][-1]) + "\n")

    g.write(str(result[-1][0]) + " ")
    g.write(str(result[-1][1]))


def SO_BAI6():
    """
    Cho số nguyên dương N (N<2.10^9). Hãy xác định xem trong phạm vi từ 1 tới N có bao nhiêu số, mà trong dạng biểu diễn nhị phân của nó có đúng K số 0 có nghĩa.
        Dữ liệu vào: Vào từ file SO.INP, gồm nhiều dòng, mỗi dòng chứa 2 số nguyên N và K (cách nhau 1 dấu cách).
        Kết quả ra: Đưa ra file SO.OUT số lượng các số tìm được ứng với một cặp N và K mỗi số trên 1 dòng. 
    Ví dụ:
    SO.INP
    18 3
    13 2
    SO.OUT
    3
    4
    """
    lines = f.readlines()

    def checkCoutZeroBinary(n, k):
        result = 0
        for i in range(1, n+1):
            binary = bin(i)[2:]
            num0 = 0
            for num in binary:
                if num == '0':
                    num0+=1
            if num0 == k:
                result+=1
        return result        
                    

    for line in lines:
        n, k = map(int, line.split())
        print(checkCoutZeroBinary(n, k))

def CHIAHET_BAI7():
    """
    Cho trước các số nguyên M, N và K ( M+N<=30; 1<=M; 0<=N; 1<=K<500). Hãy tìm:
        1. Số lượng số tự nhiên khi chia hết cho K, biểu diễn nhị phân của nó đúng M số 1 và N số 0 (không tính các số không vô nghĩa).
        2. Hãy in ra kết quả thoả 1.
        Dữ liệu vào: Cho trong file chiahet.inp gồm 1 dòng chứa 3 số M, N, K cách nhau bởi khoảng trắng.
        Dữ liệu ra: Cho trong file chiahet.out gồm 2 dòng, dòng đầu chứa số lượng tìm được, dòng thứ hai chứa một trong các số thoả mãn. Nếu không tồn tại, file chỉ chứa số 0. 
    CHIAHET.INP
    6  3  10
    CHIAHET.OUT
    6
    350 380 430 470 490 500

    Giải thích
    6 số tìm được:
    350: 101011110
    380: 101111100
    430: 110101110
    470: 111010110
    490: 111101010
    500: 111110100



    Ý tưởng:

    Một số được lưu trữ dưới dạng nhị phân:
    bit = [log2(x)] với bit và x lần lượt là không gian lưu trữ và giá trị lưu trữ

    x_max = 2^bit - 1: giá trị lớn nhất mà bit lưu được
    x_min = 2^bit-1 : giá trị nhỏ nhất mà bit lưu được

    Đề bài cho INP: M, N là tổng số bit cần để lưu giá trị cần kiểm:
    Duyệt i từ x_min  ->  x_max:
        Kiểm tra x % k == 0 và N số 0:
            Lưu giá trị

    In kết quả

    """

    m, n, k = map(int, f.readline().split())

    def checkBit(x:int):
        bit = bin(x)[2:]
        num0 = 0
        for num in bit:
            if num == "0":
                num0 += 1
        if num0 == n:
            return True
        return False

    start = int(pow(2, m + n - 1))
    end = int(pow(2, m + n)) - 1

    result = []

    for i in range(start, end+1):
        print(i)
        if i % k == 0:
            if checkBit(i):
                result.append(i)

    g.write(str(len(result)) + "\n")
    for i in range(len(result)-1):
        g.write(str(result[i]) + " ")
    g.write(str(result[-1]))




def VITRISO_BAI8():
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

    vitri = -1
    s = -1


    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
            
        if vitri != -1:
            s += b
            if s <= 0:
                vitri = -1
                s = -1
                if a+b>0:
                    vitri = i
                    s = a+b
        
        elif a+b > 0:
            vitri = i
            s = a+b

    g.write(str(vitri+1))





    
def GIAITHUA_BAI9():
    """
    Bài 9: Phân tích N! thành thừa số nguyên tố
    Giai thừa N tăng rất nhanh, VD: 5! = 120, 10!=362880. Một cách để xác định các số lớn như vậy, người ta chỉ ra số lần xuất hiện các số nguyên tố trong phân tích của nó ra thừa số nguyên tố. VD: 825 có thể xác định như sau: (0 1 2 0 1) có nghĩa là 825=20 . 31 . 52 . 70 . 111.
        Cho một số nguyên dương N<=1000. Hãy biểu diễn N! dưới dạng số lần xuất hiện các số nguyên tố trong phân tích số n! ra các thừa số nguyên tố.
        Dữ liệu vào: File GIAITHUA.INP chỉ gồm số n.
        Kết quả ra: File GIAITHUA.OUT dãy các số là số lần xuất hiện các số nguyên tố trong phân tích của N! 
        Ví dụ:
    GIAITHUA.INP
    GIAITHUA.OUT
    10
    8 4 2 1

    Ý tưởng:
    Duyệt từ 1 đến n: (i)
        tsnt = Phân tích thừa số nguyên tố của i
        đếm số lần xuất hiện của 2, 3, 5, 7, 11 trong tsnt

    Nếu 11 có giá trị bằng không thì không phải hiện thị:
        In kết quả: Kết thúc

    """

    n = int(f.readline())

    def tsnt(x):
        result = []
        for i in range(2, x):
            while x % i == 0:
                result.append(i)
                x //= i
        if len(result) == 0:
            return [x]
        return result

    result = {}

    for i in range(2, n+1):
        number = tsnt(i)
        for k in number:
            if k in result:
                result[k] += 1
            else:
                result[k] = 1

    for i, j in result.items():
        g.write(str(j) + " ")


def main():
    string()
    f.close(); g.close()

if __name__ == "__main__":
    main()