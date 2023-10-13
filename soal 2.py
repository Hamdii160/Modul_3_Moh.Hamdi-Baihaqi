x = int(input("Masukkan nilai: "))

if x <= 1:
    print("Tidak ada bilangan prima yang kurang dari atau sama dengan", x)
else:
    print("Bilangan prima antara 2 dan", x, "adalah:")
    for i in range(2, x + 1): 
        saya = True 
        for j in range(2, i): 
            if i % j == 0:
                saya = False
                break
        if saya :                    #mebuat percabangan lagi untuk mengubah ouput bilangan prima kebawa menjadi ke menyamping
            print(i, end=' ')