animals = {}
an1 = {}
an2 = {}

with open("twitt_1new.csv", "r", encoding="UTF-8") as f:
    next(f)
    for line in f:
        an_type = line.split(";")[1].strip().lower()
        tone = int(line.split(";")[4].strip().lower())
        animals.setdefault(an_type, 0)
        an1.setdefault(an_type, 0)
        animals[an_type] += tone
        an1[an_type] += tone

with open("twitt_2new.csv", "r", encoding="UTF-8") as f:
    next(f)
    for line in f:
        an_type = line.split(";")[1].strip().lower()
        tone = int(line.split(";")[4].strip().lower())
        animals.setdefault(an_type, 0)
        an2.setdefault(an_type, 0)
        animals[an_type] += tone
        an2[an_type] += tone

print(animals)
print(an1)
print(an2)
print(f'В целом самое доброе животное: {max(animals, key=animals.get)}')
print(f'Самое доброе животное на первом дубе: {max(an1, key=an1.get)}')
print(f'Самое доброе животное на втором дубе: {max(an2, key=an2.get)}')