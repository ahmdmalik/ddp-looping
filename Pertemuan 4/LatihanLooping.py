print("----------cetak 1 s/d 20----------")
angka = 20
for no in range(angka):
    no += 1 # NO = NO + 1
    print("angka", no)

    print("----------cetak bilangan genap 1 s/d 20----------")
    bil = 20
    for no in range(bil):
        no += 1 # no = no + 1
        if(no % 2 == 0):
            print("bilangan genap", no)