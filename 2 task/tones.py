pos = [" хорош", " спасибо", " вдохновен", " радост", " энерг", " красив", " прекрасн", " вкусн", " забавн", " мил", " уютн", " весел", " мелодичн", " свободн", "ласков", "впечатл", "лучш", "талант"]
neg = [" ненави", " безответствен", " наказан", " жестокост", " убийств", " бед", " виновн", " варварств", " грустно", ' печально', ' плох', ' фейк']

with open("C:/Users/Olga/Downloads/tweeter_dub1.csv", "r", encoding="UTF-8") as f:
    with open("twitt_1new.csv", "w", encoding="UTF-8") as fin:
        next(f)
        fin.write("Автор поста;Вид автора поста;текст поста;дата поста;Тональность\n")
        for line in f:
            text = " " + line.split(";")[2].strip().lower()
            tone = 0
            for find in pos:
                tone += text.count(find)
            for find in neg:
                tone -= text.count(find)
            fin.write(line.strip() + ";" + str(tone) + "\n")
