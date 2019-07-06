def jajan(tanggal, uang):
    per_mie = 2500
    if (tanggal % 2) != 0: #ganjil
        normal = uang/per_mie
        bonus = normal/3
        total = normal+bonus
        print('Total mie tanggal ganjil :',int(total))
    if (tanggal % 2) == 0: #genap
        normal = uang/per_mie
        bonus = normal/4
        total = normal+bonus
        print('Total mie tanggal genap :',int(total))
    if (tanggal % 5) == 0:
        if (bonus % 2) == 0:
            bonus = bonus*10
        else:
            bonus = bonus*5
            total = normal+bonus
        print('Total mie tanggal kelipatan 5 :',int(total))

# contoh
jajan(24,500000)