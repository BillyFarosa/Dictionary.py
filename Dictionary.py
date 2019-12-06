kontak = {}
while True:
    print("")
    c = input("T)ambah, E)dit, H)apus, C)ari, L)ist, K)eluar: ")
    if c.lower() == 'k':
        print("CREATE by : BILLY FAROSA")
        break
    elif c.lower() == 'l':
        if kontak.items() :
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
        else :
             print ("\\-------------------------DATA NILAI AKHIR MAHASISWA----------------------------------/")
             print ("****************************************************************************************")
             print ()
             print ()
             print ("========================================================================================")
             print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
             print ("========================================================================================")
             print ("                                  Tidak Ada Data")
             print("========================================================================================")
    elif c.lower() == 't':
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
            akhir = ((nilaitgs)*30/100 + (nilaiuts)*35/100 + (nilaiuas)*35/100)
            kontak[nama] = nim, nilaiuts, nilaiuas, nilaitgs, akhir
        else:
            print("Kontak {0} tidak ada".format(nama))
    elif c.lower() == 'h':
        print("Hapus Kontak")
        nama = input("Nama: ")
        if nama in kontak.keys():
            del kontak[nama]
        else:
            print("Kontak {0} tidak ada".format(nama))
    elif c.lower() == 'c':
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
