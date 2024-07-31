def CSNT(a: int, b: int): # https://ucode.vn/problems/bai-1-liet-ke-cac-so-nguyen-to-trong-doan-lr-156140
    """
    Kiểm tra trong đoạn a, b có những số nguyên tố nào
        Input: a, b (int) : Khoảng kiểm tra
        Output: arr (list) : Các số nguyên tố trong đoạn [a, b]
    Ý tưởng:
        Duyệt các số trong arr = [A, B] 
            Kiểm tra arr[i] có phải là số nguyên tố:
                Đúng 
                {
                    Lưu vào danh sách kết quả
                }
        In kết quả
    Thuật toán:
        for i [A, B]:
            if arr[i] là số nguyên tố:
                result.append(arr[i])
        return result    
    """

    def prime(x):
        if x in [2, 3]:
            return True
        elif x < 2 or x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x**0.5)+1, 6):
            if x % i == 0 or x % (i + 2) == 0:
                return False
        return True
    result = []
    for i in range(a, b+1):
        if prime(i):
            result.append(i)
    return result
def CHUSO(m: int, n: int, k: int) -> str: # https://ucode.vn/problems/bai-2-tim-k-chu-so-cuoi-cung-cua-mn-156141
    """
    Tìm k số sau cùng của m^n
        Input: M (cơ số) N (mũ số) K (số chữ số sau cùng của M ^ N)
        Output: K chữ số sau cùng của M ^ N
    Ý tưởng:
        M^N = M.M.M.M....M_N = abcd..
        Chỉ lấy k số sau cùng ở mỗi phép tích để tính toán
        cho m, n, k = 9, 5, 3; t chỉ có k số
        t1 = 1 
        t2 = t1 * 9 (t2 = 9)
        t3 = t2 * 9 (t3 = 81)
        t4 = t3 * 9 (t4 = 729)
        t5 = t4 * 9 (t5 = 656)
        t6 = t5 * 9 (t6 = 049)
        Nếu chiều dài của t > k: thì lấy khoảng theo CT:
            t = t[len(t)-k:]    
    """
    t = "1"
    for _ in range(n):
        t = str(int(t)*m)
        if len(t) > k:
            t = t[len(t)-k:]
    return t
def XAUCON(s: str): # https://ucode.vn/problems/bai-3-dem-so-luong-xau-con-lien-tiep-khac-nhau-cua-s-158285
    """
    Đếm số lượng xâu con liên tiếp khác nhau trong chuỗi
    
    Ý tưởng:
        Tạo ra các xâu liên tiếp bằng cách duyệt bằng 2 con trỏ
        Nếu xâu chưa có trong ds:
            Thêm vào ds
        In số lượng kết quả
    """
    result = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            char = s[i:j]
            if char not in result:
                result.append(char)
    result = len(result)
    return result
def SXPS(n: int, k: int) -> str: # https://ucode.vn/problems/bai-4-phan-so-thu-k-trong-tap-fn-158286
    """
    Trong danh sách có tất cả các phân số trong đoạn [0, 1] với mẫu số không quá *n. In ra vị trí *k của danh sách sau khi sắp xếp.
    
    Ý tưởng:
        Để các giá trị tạo được luôn nhỏ hơn 0 thì mẫu lớn hơn tử
        Dùng 2 dòng for
            với for i (0 -> n): tử
                for j (i+1, n): mẫu:
                    thêm vào ds_phanso ("i/j")
                    thêm vào ds_thapphan i/j
        Sắp xếp ds_thapphan:
            Khi sắp xếp thapphan thì sắp xếp luôn ds_phanso
        In vị trí thứ k trong ds_phanso
    """
    phanso = []
    dec = []
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if i / j not in dec:
                phanso.append(f"{i}/{j}")
                dec.append(i / j)

    def sapxep(arr: int, lst: str):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst
    result = sapxep(dec, phanso)
    return result[k - 1]
def NGTOFIB(n: int): # https://ucode.vn/problems/bai-5-tim-so-nguyen-x-thoa-man-156139
    """
    Trong X trong đoạn từ 10 -> n.
    Tìm số thõa:
        + X là số nguyên tố
        + X là số fibonacci
        + 1 hoán vị của X là số nguyên tố
    Input: n (int)
    Output:
        [
            [X_1, X_1hv]
            [X_2, X_2hv]
            [...]
            [X_k, X_khv]
        ]
    Ý tưởng:
        Tạo ra các số fib có giá trị từ 10 đến N:
            Kiểm tra số nguyên tố
            Tạo hoán vị:
                Nếu hoán vị là số nguyên tố thì dừng hoán vị
                    Thêm vào ds kết quả: Số đang kiểm tra; Hoán vị là số nguyên tố
        In kết quả trong ds kết quả
    """
    def matrix_mul(a, b):
        arr = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    arr[i][j] += a[i][k] * b[k][j]
                    arr[i][j] %= MOD
        return arr
    def matrix_root(a):
        return matrix_mul(a, a)
    def binpow(a, n):
        if n == 1:
            return a
        tmp = binpow(a, n // 2)
        if n % 2 == 1:
            return matrix_mul(matrix_root(tmp), a)
        else:
            return matrix_root(tmp)
    def is_prime(x):
        if x in [2, 3]:
            return True
        if x < 2 or x % 2 == 0 or x % 3 == 0:
            return False
        for i in range(5, int(x ** 0.5) + 1, 6):
            if x % i == 0 or x % (i + 2) == 0:
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
                backtrack(path + options[i], options[:i] + options[i + 1:])
        backtrack("", x)
        return result
    num = 0
    index = 7
    result = []
    fib = [[1, 1], [1, 0]]
    MOD = 10000000000
    while num < n:
        num = binpow(fib, index)[0][1]  # Fib
        if num > n:
            break
        index += 1
        # -----------------------
        if is_prime(num) and len(hoanvi(num)) == 2:
            nums = hoanvi(num)
            result.append(nums)
    return result
def SO(n: int, k: int): # https://ucode.vn/problems/bai-6-day-nhi-phan-co-dung-k-so-0-co-nghia-158499
    """
    Kiểm tra từ 1 đến n có bao nhiêu số khi biểu diễn ở dạng nhị phân có đúng k số 0 (có nghĩa)
    
    Ý tưởng:
        Kiểm tra các số từ 1 đến n:
            Chuyển *num thành số nhị phân
            Kiểm tra số nhị phân trong *num có bao nhiêu số 0:
            Kiểm tra nếu tổng số 0 = k:
                count += 1
        In count
    """
    count = 0
    for i in range(1, n + 1):
        binary = bin(i)[2:]
        num0 = 0
        for num in binary:
            if num == '0':
                num0 += 1
        if num0 == k:
            count += 1
    return count
def CHIAHET(m: int, n: int, k: int): # https://ucode.vn/problems/bai-7-chia-het-cho-k-158500
    """
    Cho M số 1; N số 0 thuộc mã nhị phân
    Tìm các số thập phân chuyển từ nhị phân chia hết cho k
    """
    
    def checkBit(x: int) -> bool:
        bit = bin(x)[2:]
        num0 = bit.count('0')
        return num0 == n

    start = int(pow(2, m + n - 1))
    end = int(pow(2, m + n)) - 1
    result = []
    for i in range(start, end + 1):
        if i % k == 0:
            if checkBit(i):
                result.append(i)
    return result
def VITRISO(n: int, arr: list): # https://ucode.vn/problems/bai-8-tong-duong-cac-so-tren-vong-tron-158287
    """
    Tìm vị trí index mà tổng từ index cho đến hết là một số dương
    Input: n (int): Chiều dài danh sách; arr (list): Danh sách cần kiểm tra
    Output: index (int)
    """
    if sum(arr) < 0:
        return 0
    else:
        vitri = -1; s = -1
        for i in range(n - 1):
            a = arr[i]
            b = arr[i + 1]

            if vitri != -1:
                s += b
                if s <= 0:
                    vitri = -1
                    s = -1
                    if a + b > 0:
                        vitri = i
                        s = a + b

            elif a + b > 0:
                vitri = i
                s = a + b

        if vitri == -1:
            return 0
        return vitri + 1
def GIAITHUA(n): # https://ucode.vn/problems/bai-9-phan-tich-n-thanh-thua-so-nguyen-to-158288
    """
    Cho n!, hãy chuyển nó về thành thừa số nguyên tố và trả về dưới dạng
    [2: số lượng, 3: số lượng, 5:....] (chỉ in số lượng)
    Input: n (int)
    Output: [a2, a3, a5, a7, a...] (list)       
    """
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
    for i in range(2, n + 1):
        number = tsnt(i)
        for k in number:
            if k in result:
                result[k] += 1
            else:
                result[k] = 1
    content = []
    for i, j in result.items():
        content.append(j)
    return content

def BHK(n: int): # https://ucode.vn/problems/bai-10-bay-hai-khong-158559
    list_num = [2, 7]
    while list_num:
        if list_num[0] % n == 0:
            return list_num[0]
        for num in "027":
            list_num.append(int(str(list_num[0]) + num))
            if int(str(list_num[0]) + num) % n == 0:
                return int(str(list_num[0]) + num)
        list_num.pop(0)

def ONES(n: int): # https://ucode.vn/problems/bai-17-so-mot-159012
    """
    Cho số nguyên dương N, hãy tính (11111....N) ^ 2    
    """
    return pow(int("1" * n), 2)

def GOLD(n, arr): # https://ucode.vn/problems/bai-11-alibaba-va-40-ten-cuop-158504
    """
    Tìm đoạn trong danh sách có tổng lớn nhất
    Input: n (int) -> Chều dài danh sách; arr (list) -> Danh sách cần tìm
    Output: [s, a, b] (list)(int) -> Tổng lớn nhất tìm được; Vị trí đầu, vị trí cuối
    """
    ds = [arr[0]]
    check = [False for i in range(n)]
    for i in range(1, n):
        num = arr[i] + ds[-1]
        if num > arr[i]:
            ds.append(num)
            check[i] = True
        else:
            ds.append(arr[i])

    # Tim max
    a, b = 0, 0
    m = ds[0]
    for i in range(1, n):
        if m < ds[i]:
            m = ds[i]
            b = i + 1
    for i in range(b, -1, -1):
        if not check[i]:
            a = i + 1
            break
    return [m, a, b]

def STRING(k: int, s1: str): # https://ucode.vn/problems/bai-12-string-158560: 
    """
    Ban đầu có một chuỗi s bị cắt tại vị trí k. Phần bị cắt của s từ k đến hết được đưa lên đầu của chuỗi s. Ta có chuỗi s1
    Input: Vị trí cắt k (int); Cho chuỗi s1 (str)
    Output: Chuỗi s1
    Ví dụ: 
        s = OLYMPIC
        s1 = MPICOLY
        k = 3
    """
    point = len(s1) - k % len(s1)
    return s1[point:] + s1[:point]

def LATGACH(arr: list, n: int, m: int): # https://ucode.vn/problems/bai-14-lat-gach-158938
    """
    Cho một danh sách hãy kiểm tra xem có bao nhiêu ô đen và ô trắng
    Input:
        n: hàng
        m: cột
        arr: danh sách kiểm tra
    Output:
        Số lượng ô đen, và ô trắng
    
    Ý tưởng:
    Ta có: 
        Ô đen:
            [
                3, 1
                0, 2
            ]
        Ô trắng:
            [
                2, 0
                1, 3
            ]
    Duyệt ds bằng 2 con trỏ:
        i, j (i duyệt từ hàng) (j duyệt từng cột):
        Nếu vị trí duyệt gặp các giá trị của Ô theo yêu cầu:
            Tăng số lượng +1 của Ô đen, hoặc Ô trắng
        In kết quả

    """
    black, white = 0, 0
    for i in range(n - 1):
        for j in range(m - 1):
            # Check Pixel Black
            if arr[i][j] == 3 and arr[i][j + 1] == 1 and arr[i + 1][j] == 0 and arr[i + 1][j + 1] == 2:
                black += 1
            # Check Pixel White
            elif arr[i][j] == 2 and arr[i][j + 1] == 0 and arr[i + 1][j] == 1 and arr[i + 1][j + 1] == 3:
                white += 1
    return black, white

def CARO(arr: list):
    """
    Cho một ma trận nhị phân
    Tìm số 1 liên tiếp lớn nhất ở trên hàng ngang, đường chéo, hàng dọc
    
    Ý tưởng:
        Duyệt danh sách: i, j
            Nếu tại vị trí arr[i, j] == 1
                Duyệt các số 1 liên tiếp theo: (Duyệt từ trên xuống)
                    Lưu vào danh sách
                        Hàng ngang, Duyệt hàng dọc, duyệt đường chéo trái, duyệt đường chéo phải
        In ra kết quả lớn nhất
    """
    n = len(arr)
    max_value = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                x = 1
                count = 1
                # Kiểm tra hàng ngang
                while j + x < n and arr[i][j + x] == 1:
                    count += 1
                    x += 1
                    if max_value < count:
                        max_value = count

                # Kiểm tra hàng dọc
                x = 1
                count = 1
                while i + x < n and arr[i + x][j] == 1:
                    count += 1
                    x += 1
                    if max_value < count:
                        max_value = count

                # Kiểm tra đường chéo trái
                count = 1
                x = 1
                while i + x < n and j - x >= 0 and arr[i + x][j - x] == 1:
                    count += 1
                    x += 1
                if count > max_value:
                    max_value = count

                # Kiểm tra đường chéo phải
                x = 1
                count = 1
                while i + x < n and j + x < n and arr[i + x][j + x] == 1:
                    count += 1
                    x += 1
                    if max_value < count:
                        max_value = count
    return max_value

def MATKHAU(s: str): # https://ucode.vn/problems/bai-20-mat-khau-159020
    """
    Cho một xâu s, hãy kiểm tra có bao nhiêu mật khẩu liên tiếp từ s là mật khẩu mạnh:
        Có chữ thường
        Có chữ hoa
        Có số
        Chiều dài từ 6 trở đi
    
    Ý tưởng:
        Dùng 2 con trỏ để tạo ra các chuỗi liên tiếp:
            Kiểm tra chuỗi có phải mật khẩu mạnh hay không:
                Đúng 
                {
                Biến đếm +1
                Nếu mật khẩu hiện tại đã đúng, toàn bộ mật khẩu sau sẽ đúng:
                Biến đếm + (len(s) - vị trí hiện tại)
                Kết thúc kiểm tra con trỏ thứ 2, -> Tiếp tục kiểm tra con trỏ thứ 1 (i+1)    
                }
        In kết quả
    """
    def strongPassword(s: str):
        a, A, n = False, False, False

        if len(s) >= 6:
            for char in s:
                if ord(char) in range(97, 123):
                    a = True
                elif ord(char) in range(65, 91):
                    A = True
                elif ord(char) in range(48, 58):
                    n = True
        if a and A and n:
            return True
        return False
    count = 0
    for i in range(len(s)):
        for j in range(i + 6, len(s) + 1):
            if strongPassword(s[i:j]):
                count += 1
                count += len(s) - j
                break
    return count

def main():
    f, g = open("input.txt", "r"), open("output.txt", "w")
    help(CSNT)
    
    f.close(); g.close()

if __name__ == "__main__":
    main()