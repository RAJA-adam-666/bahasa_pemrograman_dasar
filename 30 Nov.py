number_list= [] #siapkan list kosong
n = int(input("input ukuran list"))
jum = 0
print ("\n")
for i in range(0,n):
    print("input nilai pada index ke-:",i)
    list_item = int(input())
    jum = jum+list_item
    number_list.append(list_item) #memasukan kedalam list
    
print("data list:",number_list)
print("jumlah:",jum)

#manipulasi perulangan untuk tipe data dictionary
transaction_data ={
    "id" : 1,
    "source_country" : "United Kingdom",
    "target_country" : "Indonesia",
    "currency" : "GBP",
    "amount" : 1000.00,
    "target_currency" : "Rp",
    "fx_rate" : 19972.91,
    "platform" : "mobile",
    
}
print(transaction_data)
print()
for key in transaction_data:
    print(key,";",transaction_data[key])
    
#neested loop
for i in range(1,5,1):
    for j in range(0,3,1):
        print(i*j, end=" ")
    print()

#buat pola segitiga dengan perulangan
k=1
baris=int(input('tentukan baris dari segitiga:'))
for i in range(1,baris+1):
    print(' ' * (baris - i),end="")
    for j in range(1,i+1):
        print(k, end=" ")
        k=k+1
    print()
