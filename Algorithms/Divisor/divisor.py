f = open("input.txt", "r")

g = open("output.txt", "w")


n = int(f.readline())


def divisor(n):
    c, s = 1, 1

    for i in range(2, int(n**0.5)+1): # Duyệt các số từ 2 đến n**0.5

        if n % i == 0: # Kiểm tra ước
            c += 1
            s += i

            # Kiểm tra ước đối
            if (n / i) != i:
                c+=1
                s += n / i

    return [c,int(s)]


num = divisor(n)

g.write(str(num[0])+ "\n")

g.write(str(num[1]))



f.close(); g.close()


