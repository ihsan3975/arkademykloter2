print('masukan nilai :')
count = int(input())
n = 0
while (count != 1):    
    if (count % 2) == 0:
        count = count/2
        n = n+1
        print(count)
    else:
        count = 3*count+1
        n = n+1
        print(count)
print('Bilangan Asli dengan operasi terbanyak =', n)