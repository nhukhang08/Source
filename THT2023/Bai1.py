"""_summary_
Đề bài:
Input: 
1 2 2 1 1 3
3 2
Output:
3

Chèn số 2 vào vị trí thứ x = 3 ta có 1 2 2 2 1 1 3
ta có 3 số 2 liên tiếp thì ta xóa chúng đi: 1 1 1 3
Tiếp tục có 3 số 1 giống nhau: 3

Không còn các giá trị nào giống nhau liên tiếp, ta in ra kết quả: 3

"""
"""
Ý tưởng:

Chèn số k = 2 vào vị trí x = 3: s = 1, 2, 2, 2, 1, 1, 3
Ta sẽ dùng hàm để kiểm tra có giá trị nào giống nhau 3 lần liên tiếp hay không:
    {
        Nếu có, thì xóa khoảng đó đi khỏi danh sách
    }
    else
    {
        In kết quả
    }
Function: CheckResultGame(s: arr)

s = [1, 2, 2, 2, 1, 1, 3]
1:
{
    left = -1
    right = -1
}
2:
{
    left = 1
    right = -1
}
3:
{
    left = 1
    right = 3
}
4:
{
    
}
Duyệt toàn bộ danh sách:
    Kiểm tra các cặp số (a, b):
    {
        left = -1
        
        Nếu a = b và {left chưa xét} thì lưu vị trí của a:
        {
            left = i_a
        }
        elif Nếu a = b và left đã xét thì lưu vị trí của b:       
        {
            right = i_b     
        }
        elif Nếu left và right đã xét:
        { Kết thúc vòng lặp

            Xóa khoảng đã xác định
            Trả kết quả 
        }

        
    }
                                
"""
def CheckResultGame(s: list):
    left = -1
    right = -1
    
    for i in range(len(s)-1):
        a = s[i]
        b = s[i+1]
        
        if a == b and left == -1:
            left = i
        elif a == b and left != -1:
            right = i+1
        elif left != -1 and right != -1:
            return s[:left] + s[right+1:]
        else:
            left = -1
            right = -1
        
        if i == len(s) - 1:
            return True

f = open("CANDYCRUSHSAGA.INP", "r")
g = open("CANDYCRUSHSAGA.OUT", "w")

s = list(map(int, f.readline().split()))
x, k = map(int, f.readline().split())
s.insert(x, int(k))

while True:
    if type(CheckResultGame(s)) == type([1]):
        s = CheckResultGame(s)
    else:
        for i in range(len(s)-1):
            g.write(str(s[i])+ " ")
        g.write(str(s[len(s)-1]))
        break

f.close(); g.close()