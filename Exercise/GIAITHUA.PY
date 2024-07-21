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

f = open("GIAITHUA.INP", "r")
g = open("GIAITHUA.OUT", "w")

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

num = [0, 0, 0, 0, 0]

for i in range(1, n+1):
    number = tsnt(i)
    for k in number:
        if k == 2:
            num[0] += 1
        if k == 3:
            num[1] += 1
        if k == 5:
            num[2] += 1
        if k == 7:
            num[3] += 1
        if k == 11:
            num[4] += 1

num.pop()
for i in range(len(num)-1):
    g.write(str(num[i]) + " ")
g.write(str(num[-1]))
        
f.close(); g.close()