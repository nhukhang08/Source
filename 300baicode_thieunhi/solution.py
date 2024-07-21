# https://300baicode.com/
from typing import Tuple, List, Any
def twosum(nums: list, target: int) -> list:
    """
    Cho một mảng số nguyên (arr) và một số nguyên (target)
    hãy trả về hai chỉ số của mảng số nguyên sao cho tổng của nó bằng target.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Ý tưởng:
        Duyệt từ chỉ số 0 đến hết:
            Chọn phần tử đầu tiên: Sau đó + với các số tiếp theo:
                Nếu tổng vừa tính = target:
                    thì lưu chỉ số
        In kết quả
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def AddTwoNumbers(l1: list, l2: list) -> list:
    result = []
    lenght = len(l1)

def ValidParentheses(s: str) -> bool:
    """
    Cho chuỗi s: = {'(', ')', '{', '}', '[', ']'}
    Kiểm tra tính hợp lệ của chuỗi s

    Input: s = "()"
    Output: true

    Input: s = "()[]{}"
    Output: true

    Input: s = "(]"
    Output: false

    Input: s = "([)]"
    Output: false

    Ý tưởng:

        Duyệt toàn bộ chuyển
            Kiểm tra mỗi khi gặp một ngoặc mở: lưu vào danh sách ngoặc đóng
            Khi gặp ngoặc đóng thì kiểm tra trong danh sách NGOAI CUNG có tồn tại ngoặc đóng không
                Sai: return False

    Nếu danh sách rỗng:
        return true
    """
    if len(s) % 2 != 0:
        return False
    stack = []
    for ch in s:
        if ch in ["(", "[", "{"]:
            if ch == "(":
                stack.append(")")
            if ch == "[":
                stack.append("]")
            if ch == "{":
                stack.append("}")

        if ch in [")", "]", "}"]:
            if len(stack) == 0:
                return False
            if stack[-1] == ch:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True


def MergeTwoSortedLists(list1: list, list2: list) -> list:
    if not list1:
        return list2
    if not list2:
        return list1
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
    return result


def BestTimeToBuyAndSellStock(prices: list) -> int:
    profit = 0
    min_price = float("inf")

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price
    return profit


def ValidPalindrome(s: str) -> bool:
    string = ""
    for char in s:
        if char.isalnum():
            string += char.lower()
    s = string
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True


def InvertBinaryTree(root: list) -> list:
    def nTHTree(n: int) -> tuple[int, list[Any]]:
        point = 0
        square = []
        while n > 0:
            n = n - pow(2, point)
            if n >= 0:
                square.append(pow(2, point))
            point += 1
        return len(square), square

    loop, index = nTHTree(len(root))
    result = []
    for i in range(loop):
        group = root[index[i] - 1:index[i] * 2 - 1]
        for num in group[::-1]:
            result.append(num)
    return result

def ValidAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    s, t = sorted(s), sorted(t)
    if s == t:
        return True
    return False

def BinarySearch(nums: list, target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        point = (l + r) // 2

        if nums[point] < target:
            l = point + 1
        elif nums[point] > target:
            r = point - 1
        else:
            return point
    return -1
            
    

def main():
    output = BinarySearch([5], 5)
    print(output)


if __name__ == "__main__":
    main()