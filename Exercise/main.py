
def string():
    f = open("input.txt", "r")
    g = open("output.txt", "w")
    k = int(f.readline())
    char = f.readline()
    result = []
    for i in range(len(char)):
        result.append(char[(k + i) % len(char)])

    result = "".join(result)

    g.write(str(result))

    f.close(); g.close()



def main():
    string()

if __name__ == "__main__":
    main()