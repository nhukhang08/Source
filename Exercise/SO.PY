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
with open("SO.INP", "r") as file:
    lines = file.readlines()

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