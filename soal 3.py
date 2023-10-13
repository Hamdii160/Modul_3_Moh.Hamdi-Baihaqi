def hitung_denda(lama_peminjaman):
    denda_per_hari = 2000
    denda_per_minggu = 5000
    total_denda = 0

    if lama_peminjaman > 7:
        total_denda += (lama_peminjaman - 7) * denda_per_hari

    total_denda += (lama_peminjaman // 7) * denda_per_minggu

    return total_denda

while True:
    lama_peminjaman = int(input("Masukkan lama peminjaman buku (dalam hari): "))
    denda = hitung_denda(lama_peminjaman)
    print("Denda yang harus dibayar: Rp{}".format(denda))

    ulangi = input("Apakah Anda ingin menghitung lagi? (ya/tidak): ")
    if ulangi.lower() != "ya":
        break
