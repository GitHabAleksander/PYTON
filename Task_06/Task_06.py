n = int(input())
reshka = True
i = 1
while reshka:
    if n > 0:
        n -= i
    else:
        reshka = False
    i += 1
print(i)
        