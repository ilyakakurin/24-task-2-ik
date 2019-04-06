n = int(input()) 
k = 0
while k % 5 == 0:
  k = k+ 1
  n = n // 5
if k == 1:
    print(k)
else:
    print('Не существует')
