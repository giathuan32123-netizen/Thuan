try:
    Van = float(input("nhap diem van: "))
    Toan = float(input("nhap diem toan: "))
    Anh = float(input("nhap diem anh: "))
except ValueError:
    print('sai kieu nhap lieu')
else:
    if any(x < 0 or x > 10 for x in (Van, Toan, Anh)):
        print('sai kieu du lieu')
    else:
        dtb = (Van + Toan + Anh) / 3
        if dtb >= 9:
            print('xuat sac')
        elif dtb >= 8:
            print('gioi')
        elif dtb >= 7:
            print('kha')
        elif dtb >= 5:
            print('tb')
        else:
            print('yeu')


a = 2
while a <= 10:
    print(float(a), end='')
    a += 2

b = 3
while b <= 18:
    print(float(b), end='')
    b += 3
c = 5
while c <= 100:
    print(float(c), end='')
    c += 5

d = 1
while d = 100:
    print(float(d), end='')