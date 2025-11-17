import math

try:
    van = float(input('Nhập điểm văn: '))
    toan = float(input('Nhập điểm toán: '))
    anh = float(input('Nhập điểm anh: '))
except ValueError:
    print('Lỗi nhập sai kiểu dữ liệu')
else:
    DTB = (van + toan + anh) / 3
    if van < 0 or van > 10:  
        print("Nhập điểm văn ko hợp lệ")
    elif toan < 0 or toan > 10:
        print("Nhập điểm toán ko hợp lệ")
    elif anh < 0 or anh > 10:
        print("Nhập điểm anh ko hợp lệ")
    else:
        if DTB >= 9:
            print('Xếp loại xuất sắc')
        elif DTB >= 8 and DTB < 9:
            print('Xếp loại giỏi')
        elif DTB >=7 and DTB < 8:
            print('Xếp loại khá')
        elif DTB >= 5 and DTB < 7:
            print('Xếp loại trung bình')
        else: 
            print('Xếp loại yếu')


    # vd1: In ra các số chẵn từ 2 đến 10
            i = 2
            while i <= 10:
                print(i, end=" ")
                i += 2
    # vd2: In ra các bội số của 3 từ 3 đến 18
            i = 3
            while i <= 18:
                print(i, end=" ")
                i += 3
    # vd3: Tính tổng các số từ 1 đến 100
            i = 5
            while i <= 100:
                 print(i, end=" ")
                 i += 5
    # vd4: Tính giai thừa của một số nguyên dương n
            i = 1
            while i <= 99:
                print(i, end="+")
                i += 1
            print(100)
            

