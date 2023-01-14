rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i = 0
while True:
    end = i + 2
    if end >= len(rows):
        end = len(rows)
    tmps = rows[i:end]
    print(tmps)
    if end == len(rows):
        break
    i = end
