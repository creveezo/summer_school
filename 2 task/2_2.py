dates = {}
total_count = 0
av_abs = 0.420849420849421

with open("twitt_1new.csv", "r", encoding="UTF-8") as f:
    next(f)
    for line in f:
        time = line.split(";")[3]
        tone = int(line.split(";")[4])
        dates.setdefault(time, [0, 0])
        dates[time][0] += 1
        dates[time][1] += tone

for n, value in dates.items():
    av_day = value[1]/value[0]
    if av_day > av_abs:
        total_count += 1

print(total_count)


