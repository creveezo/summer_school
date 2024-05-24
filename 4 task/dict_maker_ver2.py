with open('dict_new.txt') as f:
    d = open("dict_new1.txt", "w")
    while True:
        word = f.readline().strip()
        if len(word) == 5:
            d.write(f"{word}\n")
