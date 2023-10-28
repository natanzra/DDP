list = ["NamaKendaraan","JenisKendaraan","ccKendaraan","WarnaKendaraan","RodaKendaraan"]
list.append("HargaKendaraan")
list.append("TipeKendaraan")
list.insert(2, "MerkKendaraan")
print(list)

pilihan= input ("**PILIH OPERASI** \n 1.Menghitung Luas Persegi \n 2.Menghitung luas lingkaran \n 3.Menghitung luas segitiga \n Masukkan pilihan """)
match pilihan:
    case "1" :
        s = int (input("Masukkan nilai sisi: "))
        persegi = s*s
        print('luas persegi', persegi)
    
    case "2" :
        r = int (input("Masukkan nilai r: "))
        phi = 3.14
        lingkaran = phi*r*r
        print('luas lingkaran', lingkaran)

    case "3" :
        alas = int (input("Masukkan nilai alas: "))
        tinggi = int (input("Masukkan nilai alas: "))
        segitiga = 1/2*alas*tinggi
        print("luas segitiga", segitiga)

    case _ :
        "pilihan tidak tersedia"