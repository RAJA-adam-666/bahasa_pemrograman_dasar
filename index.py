#Struktur IF
nilai_akhir = int(input("masukan nilai : "))
if nilai_akhir  >=100 :   
   keterangan ="asu"
   print(f"anda dinyatakan : {keterangan} dengan nilai :  {nilai_akhir}" )
elif nilai_akhir  >=60 :   
   keterangan ="kanjut"
   print(f"anda dinyatakan : {keterangan} dengan nilai :  {nilai_akhir}" )
   
else :
   keterangan ="tidak lulus"
   print(f"anda dinyatakan : {keterangan} dengan nilai :  {nilai_akhir}" )
