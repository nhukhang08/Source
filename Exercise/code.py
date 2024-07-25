f, g = open("input.txt", "r"), open("output.txt", "w")
n, m = map(int, f.readline().split())
arr = []
for line in f.readlines():
    arr.append(list(map(int, line.split())))

black, white = 0, 0
for i in range(n-1):
    for j in range(m-1):
        # check White
        if arr[i][j] == 3 and arr[i][j+1] == 1 and arr[i+1][j] == 0 and arr[i+1][j+1] == 2:
            black += 1
        elif arr[i][j] == 2 and arr[i][j+1] == 0 and arr[i+1][j] == 1 and arr[i+1][j+1] == 3:
            white += 1

g.write(str(black) + " " + str(white))

f.close; g.close()