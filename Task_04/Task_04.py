n = 385916

summ = 0
summ2 = 0

while n > 999:
    count = n % 10
    summ = summ + count
    n = n // 10
    
while n > 0:
    count = n % 10
    summ2 = summ2 + count
    n = n // 10
    
if summ == summ2:
    print("yes")
else:
    print("no")