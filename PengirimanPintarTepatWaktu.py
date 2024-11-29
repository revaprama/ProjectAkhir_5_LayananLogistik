list_pengiriman_barang = []
data_sama=set()
def input_barang():
    while True:
        nama_pengirim = input("masukkan nama pengirim: ")
        if nama_pengirim == "":
            print("nama tidak boleh kosong")
        else:
            break
    while True: 
        tempat_penjual = input("masukan tempat pengirim: ")
        if tempat_penjual == "":
            print("tidak boleh kosong")
        else:
            break
    while True:
        notelp_penjual = input("masukkan no telepon penjual: ")
        if len(notelp_penjual) != 12 or notelp_penjual == "":
            print("no telepon harus terdiri dari 12 angka")
        else:
            break
    while True:
        nama_penerima = input("masukkan nama penerima: ")
        if nama_pengirim == "":
            print("tidak boleh kosong")
        else:
            break
    while True:
        tempat_tujuan = input("masukan tempat tujuan: ")
        if tempat_tujuan == "":
            print("tidak boleh kosong")
        else:
            break
    while True:
        notelp_penerima = input("masukkan no telepon penerima: ")
        if len(notelp_penerima) != 12 or notelp_penerima == "":
            print("no telepon harus terdiri dari 12 angka")
        elif notelp_penerima == notelp_penjual:
            print("no telepon tidak boleh sama")
        else:
            break
    while True:
        nama_barang = input("masukan nama barang yang akan dikirim: ")
        if nama_barang == "":
            print("tidak boleh kosong")
        else:
            break
    while True:
        berat_barang = int(input("masukan berat barang yang akan dikirim (dalam gram):"))
        if berat_barang > 0:
            break
        else:
            print("berat barang harus melebihi 0")
    while True:
        jumlah_barang = int(input("masukan jumlah barang yang akan dikirim: "))
        if int(jumlah_barang) > 0:
            break
        else:
            print("jumlah barang harus melebihi 0")
    while True:
        no_resi = input("masukan no resi (harus terdiri dari 17 karakter): ")
        if len(no_resi) != 17 or no_resi == "":
            print("no resi harus terdiri dari 17 karakter")
        elif no_resi in data_sama:
            print("no resi tersebut sudah terdaftarkan, silahkan msukan no resi yang lain")  
        else:
            data_sama.add(no_resi)
            break
    while True:
        tanggal_pengiriman = input("masukkan tanggal pengiriman (YYYY-MM-DD): ")
        if tanggal_pengiriman == "":
            print("tidak boleh kosong")
        else:
            break
    while True:
        jarak = int(input("jarak yang akan ditempuh: "))
        if jarak > 0:
            break
        else:
            print("jarak harus melebihi 0")
    hargakm = 700
    hargagram = 5
    biaya_pengiriman = (hargakm*jarak)+(hargagram*berat_barang)
    print(f"jadi biaya pengirim = Rp. {biaya_pengiriman}")
    list_pengiriman_barang.append({
        "barang":nama_barang,
        "pengirim":nama_pengirim,
        "penjual":tempat_penjual,
        "penerima":nama_penerima,
        "tujuan":tempat_tujuan,
        "jumlah":jumlah_barang,
        "noresi":no_resi,
        "tanggal":tanggal_pengiriman,
        "jarak":jarak,
        "biaya":biaya_pengiriman,
        "tlp_penjual":notelp_penjual,
        "tlp_penerima":notelp_penerima,
        "berat":berat_barang,
    })
    return list_pengiriman_barang
def read_pengiriman():
    if list_pengiriman_barang:
        for i,barang in enumerate(list_pengiriman_barang):
            print(f"\ndata pengiriman barang ke-{i+1}")
            print("===================================================")
            print(f"nama pengirim/toko : {barang["pengirim"]}")
            print(f"alamat pengirim    : {barang["penjual"]}")
            print(f"no telepon penjual : {barang["tlp_penjual"]}")
            print(f"nama penerima      : {barang["penerima"]}")
            print(f"alamat tujuan      : {barang["tujuan"]}")
            print(f"no telepon penerima: {barang["tlp_penerima"]}")
            print(f"nama barang        : {barang["barang"]}")
            print(f"jumlah barang      : {barang["jumlah"]}")
            print(f"berat barang       : {barang["berat"]}")
            print(f"no resi barang(gram)     : {barang["noresi"]}")
            print(f"tanggal pengiriman : {barang["tanggal"]}")
            print(f"jarak(km)          : {barang["jarak"]}")
            print(f"biaya/ongkir       : {barang["biaya"]}")
            print("===================================================")
    else:
        print("data pengiriman barang masih belum ada")
def update_pengiriman(no_resi):
    for barang in list_pengiriman_barang:
        if barang["noresi"] == no_resi:
            nama_pengirim = input("masukkan nama pengirim yang baru: ") or barang["pengirim"]
            tempat_penjual = input("masukan tempat pengirim yang baru: ") or barang["penjual"]
            while True:
                notelp_penjual = input("masukkan no telepon penjual yang baru: ") or barang["tlp_penjual"]
                if len(notelp_penjual)==12:
                    break
                else:
                    print("no telepon harus terdiri dari 12 angka")
            nama_penerima = input("masukkan nama penerima yang baru: ") or barang["penerima"]
            tempat_tujuan = input("masukan tempat tujuan yang baru: ") or barang["tujuan"]
            while True:
                notelp_penerima = input("masukkan no telepon penerima yang baru: ") or barang["tlp_penerima"]
                if len(notelp_penerima)== 12:
                    break
                else:
                    print("no telepon harus terdiri dari 12 angka")
            nama_barang = input("masukan nama barang yang akan dikirim yang baru: ") or barang["barang"]
            while True:
                jumlah_barang = input("masukan jumlah barang yang akan dikirim: ") or int(barang["jumlah"])
                if int(jumlah_barang) > 0:
                    break
                else:
                    print("jumlah barang harus melebihi 0")
            while True:
                berat_barang = input("masukan berat barang yang baru: ") or int(barang["berat"])
                if int(berat_barang) > 0:
                    break
                else:
                    print("jumlah harus melebihi 0")
            tanggal_pengiriman = input("masukkan tanggal pengiriman yang baru(YYYY-MM-DD): ") or barang["tanggal"]
            hargakm = 700
            hargagram = 5
            while True:
                jarak = input("jarak yang akan ditempuh yang baru: ") or int(barang["jarak"])
                if int(jarak) > 0:
                    break
                else:
                    print("jatak harus melebihi 0")
            biaya_pengiriman = (hargakm*jarak)+(hargagram*berat_barang)
            print(f"jadi biaya pengirim = Rp. {biaya_pengiriman}")
            barang["pengirim"] = nama_pengirim
            barang["penjual"] = tempat_penjual
            barang["tlp_penjual"] = notelp_penjual
            barang["penerima"] = nama_penerima
            barang["tujuan"] = tempat_tujuan
            barang["tlp_penerima"] = notelp_penerima
            barang["barang"] = nama_barang
            barang["jumlah"] = jumlah_barang
            barang["berat"] = berat_barang
            barang["tanggal"] = tanggal_pengiriman
            barang["jarak"] = jarak
            return
    print("barang dengan no resi tersebut tidak terdeteksi")
def mencari_data_barang(no_resi):
    for barang in list_pengiriman_barang:
        if barang["noresi"] == no_resi:
            print("data barang sesuai no resi")
            print("===================================================")
            print(f"nama pengirim/toko : {barang["pengirim"]}")
            print(f"alamat pengirim    : {barang["penjual"]}")
            print(f"no telepon penjual : {barang["tlp_penjual"]}")
            print(f"nama penerima      : {barang["penerima"]}")
            print(f"alamat tujuan      : {barang["tujuan"]}")
            print(f"no telepon penerima: {barang["tlp_penerima"]}")
            print(f"nama barang        : {barang["barang"]}")
            print(f"jumlah barang      : {barang["jumlah"]}")
            print(f"berat barang       : {barang["berat"]}")
            print(f"no resi barang     : {barang["noresi"]}")
            print(f"tanggal pengiriman : {barang["tanggal"]}")
            print(f"jarak(km)          : {barang["jarak"]}")
            print(f"biaya/ongkir       : {barang["biaya"]}")
            print("===================================================")

def hapus_barang(no_resi):
    for barang in list_pengiriman_barang:
        if barang["noresi"] == no_resi:
            list_pengiriman_barang.remove(barang)
            print("data barang dengan no resi tersebut dihapus")
        else:
            print("barang dengan no resi tersebut tidak ada")
            
while True:
    print("\n===SELAMAT DATANG DI PENGIRIMAN PINTAR, TEPAT WAKTU===")
    print("1. Menambahkan barang")
    print("2. Melihat data barang")
    print("3. Mencari data barang")
    print("4. Mengedit barang")
    print("5. Menghapus barang")
    print("6. Keluar")

    pilihan = input("Pilih menu (1/2/3/4/5/6): ")
    if pilihan=="1":
        input_barang()
    elif pilihan=="2":
        read_pengiriman()
    elif pilihan == "3":
        while True:
            no_resi = input("masukan no resi barang yang ingin dicari (harus terdiri dari 17 karakter): ")
            if len(no_resi) == 17:
                mencari_data_barang(no_resi)
                break
            else:
                print("no resi harus terdiri dari 17 karakter")
        
    elif pilihan == "4":
        while True:
            no_resi = input("masukan no resi barang yang ingin diganti (harus terdiri dari 17 karakter): ")
            if len(no_resi) == 17:
                update_pengiriman(no_resi)
                break
            else:
                print("no resi harus terdiri dari 17 karakter")
    elif pilihan == "5":
        while True:
            no_resi = input("masukan no resi barang yang ingin dihapus (harus terdiri dari 17 karakter): ")
            if len(no_resi) == 17:
                hapus_barang(no_resi)
                break
            else:
                print("no resi harus terdiri dari 17 karakter")
    elif pilihan == "6":
        break
    else:
        print("input sesuai dengan yang diperintahkan :)")