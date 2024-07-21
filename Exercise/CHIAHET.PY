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

with open("CHIAHET.INP", "r") as file:
    m, n, k = map(int, file.readline().split())

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

with open("CHIAHET.OUT", "w") as file:
    file.write(str(len(result)) + "\n")
    for i in range(len(result)-1):
        file.write(str(result[i]) + " ")
    file.write(str(result[-1]))
