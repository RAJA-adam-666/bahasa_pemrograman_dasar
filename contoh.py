x =int(input("masukan senuah bilangan : "))
if x < 200:
    print(x, "nilai kurang dari 200")
    if x == 150:
        keterangan = " :sama dengan 150"
        print(x,    keterangan)
    elif x == 100:
        keterangan = " :sama dengan 100"
        print(x,    keterangan)
    elif x == 50:
        keterangan = " :sama dengan 50"
        print(x,    keterangan)
    elif x < 50:
        keterangan = " :kurang dari 50"
        print(x,    keterangan)
else:
    keterangan ="nilai yang dimasukan salah"
    print (keterangan)

print("selesai")  