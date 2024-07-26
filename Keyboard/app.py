import keyboard, threading, itertools, sys

def LoadDataFromFile(): # Chuyen du lieu tu file <data.txt> vao bien
    data = []
    with open("data.txt", "r") as file:
        line_data_file = file.readline().strip()
        data.append(line_data_file)
    max_length = max(len(element) for element in data)
    return data, max_length*2
        

def gProcessText(key): # Chuyen phim space -> " "
    if len(key) == 1:
        return key
    if key == "space":
        return " "
    return ""

def check_for_words(input_str, words): # Kiem tra word co trong input_keyboard
    for word in words:
        if word in input_str:
            return True
    return False

def check_permutations(gText, gArr): # Tao cac hoan vi tu input_keyboard
    permutations = itertools.permutations(gText)
    for p in permutations:
        p = "".join(p)
        if check_for_words(p, gArr):
            return True
    return False

input_keyboard = ""
gArr, n = LoadDataFromFile() 
gCore = True
while gCore:
    # input_keyboard <-- key
    event = keyboard.read_event()
    key = event.name
    event_type = event.event_type
    if event_type == "up":
        input_keyboard += gProcessText(key)

    # Neu chieu dai <True> thi xet hoan vi
    if len(input_keyboard) == n:
        gText = input_keyboard
        thread_check = threading.Thread(target=check_permutations, args=(gText, gArr))
        thread_check.start() 
        if check_permutations(gText, gArr):
            gCore = False
            break
        thread_check.join()
        input_keyboard = ""

if not gCore:
    sys.exit()
