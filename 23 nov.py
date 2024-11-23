#struktur perulangan for 

for i in range (1,5,0): #menandakan nilai_awal-0, nialai_akhir<5 dan step=1
    print(i)
print ("Program Selesai")

for i in range (5): #menandakan nilai_awal-0 dan step-1
    print(i)
print ("program Selesa")

for i in range (5,0.-1): #menandakan nilai_awal-1 dan
    print(i)
print ("program Selesai")

for i in range (1,5,1): #menandakan nilai_awal-0, nialai_akhir<5 dan step=1
    print(i, end=" ")
print ("\nProgram Selesai")

n = int(input("Input Batas Perulangan"))
for i in range (n): 
    print(i, end=" ")
print ("\nprogram Selesai")

#struktur penggunaan while
i=1
while(i<5):
    print(i, end=" ")
    i = i+1
print("\nProgram Selesai")

#sialahkan modifikasi program untuk mendaptkan output dengan inputan data sbb:
#nilai pertama yang dicetak
#batas perulangan
#jeda dari setiap nilai#contoh saat user menginputkan nilai pertama yang dicetak adalah 5,dengan batas
#perulangan adalah 5 dan jeda dari setiap nilai adalah 5 maka outputnya sbb;
#5 10 15 20 25

nilai_pertama = int(input("Input Nilai Pertama: "))
nilai_perulangan = int(input("Input Batas Nilai Perulangan: "))
nilai_jeda = int(input("Input jeda disetiap nilai: "))

for i in range (nilai_perulangan): 
    nilai=nilai_pertama + (i*nilai_jeda)
    print(nilai, end=" ")
print ("\nprogram Selesai")

#mencari total keseluruhan tapi masih gagal
total = (total + nilai)*3
print ("\ntotal",total)

