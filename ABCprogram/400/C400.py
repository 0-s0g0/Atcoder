a = int(input())
seen = set()

i = 1
while True:
    base = i * i * 2
    if base > a:
        break

    val = base
    while val <= a:
        seen.add(val)
        val *= 2
    i += 1

print(len(seen))
