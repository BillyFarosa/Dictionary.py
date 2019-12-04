kontak = {}
while True:
    print("")
    c = input("A)dd, E)dit, D)elete, S)earch, L)ist, Q)uit: ")
    if c.lower() == 'q':
        print("CREATE by : BILLY FAROSA")
        break
    elif c.lower() == 'l':
        print ("\\-------------------------DATA NILAI AKHIR MAHASISWA----------------------------------/")
        print ("****************************************************************************************")
        print ()
        print ()
        print ("========================================================================================")
        print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
        print ("========================================================================================")
        i=0
        for x in kontak.items():
            i+=1
            print (" |  {6:2} | {0:7s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("========================================================================================")
    elif c.lower() == 'a':
        print(" Tambah Data ")
        nama = input(" Nama: ")
        nim = input(" NIM:")
        nilaiuts = int(input (" Nilai UTS     : "))
        nilaiuas = int(input (" Nilai UAS     : "))
        nilaitgs = int(input (" Nilai Tugas   : "))
        akhir = ((nilaitgs)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100)
        kontak[nama] = nim, nilaiuts, nilaiuas, nilaitgs, akhir
    elif c.lower() == 'e':
        print("Edit Data")
        nama = input("Masukan Nama : ")
        if nama in kontak.keys():
            nim = input("NIM : ")
            nilaiuts = int(input (" Nilai UTS     : "))
            nilaiuas = int(input (" Nilai UAS     : "))
            nilaitgs = int(input (" Nilai Tugas   : "))
            kontak[nama] = nim, nilaiuts, nilaiuas, nilaitgs, akhir
        else:
            print("Kontak {0} tidak ada".format(nama))
    elif c.lower() == 'd':
        print("Hapus Kontak")
        nama = input("Nama: ")
        if nama in kontak.keys():
            del kontak[nama]
        else:
            print("Kontak {0} tidak ada".format(nama))
    elif c.lower() == 's':
        print("Search Kontak")
        nama = input("Nama: ")
        if nama in kontak.keys():
            print ("\\-------------------------DATA NILAI AKHIR MAHASISWA----------------------------------/")
            print ("****************************************************************************************")
            print ()
            print ()
            print ("========================================================================================")
            print (" |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
            print ("=======================================================================================")
            print (" | {0:7s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(nama, nim, nilaiuts, nilaiuas, nilaitgs, akhir))
        else:
            print("Kontak {0} tidak ada".format(nama))
    else:
        print("Pilih menu yang tersedia")
