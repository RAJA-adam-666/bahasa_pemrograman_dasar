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