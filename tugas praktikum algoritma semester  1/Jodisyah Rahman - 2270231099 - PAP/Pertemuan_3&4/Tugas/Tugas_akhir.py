import datetime
tanggal = datetime.datetime.now()
admin = "jodi"

print(25*"="+"""
Nama\t: Jodisyah Rahman 
NIM\t: 2270231099
Program\t: Kasir
""" + 25*"=" + "\n")

def get_login():
    print('=' * 25)
    print('halaman login kasir')
    username = input('masukan username kasir anda: ')
    password = input('masukan password: ')
 
    if username == admin and password == 'jodi123':
        print('login berhasil...\n\n')
    else:
        print('login gagal coba lagi..')
        get_login() 

def fungsibakso():
   global total_makanan
   global porsi
   global makanan

   print ("\n--------------- Menu Bakso ---------------")
   print("1. Bakso Urat - Rp 20000")
   print("2. Bakso Beranak - Rp 35000")
   print("3. Bakso Mantan - Rp 30000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       total_makanan=porsi*20000
       print (porsi," porsi Bakso Urat = Rp", total_makanan)
       makanan=("Bakso Urat")
   elif nomor==2:
       total_makanan=porsi*35000
       print (porsi," porsi Bakso Beranak = Rp", total_makanan)
       makanan=("Bakso Beranak")
   elif nomor==3:
       total_makanan=porsi*30000
       print (porsi, " porsi Bakso Mantan = Rp", total_makanan)
       makanan=("Bakso Mantan")
   else:
      total_makanan=porsi*0
      print (porsi,"tidak pesan makanan", total_makanan)
      makanan=("tidak pesan makanan")

def fungsiminuman():
   global total_minum
   global minuman
   global gelas
   print("\n-------------- Menu Minuman --------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Es Kelapa - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       total_minum=gelas*2000
       print (gelas," Es Teh = Rp", total_minum)
       minuman=(" Gelas Es Teh")
   elif nomor==2:
       total_minum=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", total_minum)
       minuman=("Es Jeruk")
   elif nomor==3:
       total_minum=gelas*4000
       print (gelas, " Gelas Es Kelapa = Rp", total_minum)
       minuman=("Es Kelapa")
   else:
      total_minum=porsi*0
      print (porsi,"tidak pesan minuman", total_minum)
      minuman=("tidak pesan minuman")

get_login()
fungsibakso()
fungsiminuman()
totalsemua=total_makanan+total_minum

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n========================================")
print("========== S T R U K   B E L I =========")
print("========================================")
print("Tanggal\t\t: " + tanggal.strftime("%d - %m - %Y %X"))
print ("Admin\t\t:",admin)
print ("Beli\t\t:",porsi,makanan,"( Rp", total_makanan,")")
print ("\t\t ",gelas,minuman,"( Rp", total_minum,")")
print ("Total\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("========================================")
print("======== T E R I M A   K A S I H =======")
print("========================================")



# main program
if __name__=='__main__':
    fungsibakso()