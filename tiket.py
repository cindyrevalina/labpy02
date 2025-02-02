# Program menghitung harga tiket bioskop dengan diskon member
def hitung_tiket():
    print("=== Program Hitung Harga Tiket Bioskop ===")
    print("Pilih tipe tiket:")
    print("1. Reguler (Rp50.000)")
    print("2. VIP (Rp100.000)")
    
    # Input tipe tiket
    tipe_tiket = input("Masukkan pilihan (1/2): ")
    
    # Input status member
    status_member = input("Apakah anda memiliki kartu member? (y/n): ")
    
    # Menentukan harga dasar menggunakan operator ternary
    harga_dasar = 50000 if tipe_tiket == "1" else 100000
    
    # Menghitung diskon menggunakan operator ternary
    diskon = 0.2 if status_member.lower() == "y" else 0
    
    # Menghitung harga akhir
    harga_akhir = harga_dasar - (harga_dasar * diskon)
    
    # Output informasi
    print("\n=== Detail Pembayaran ===")
    print(f"Tipe Tiket: {'Reguler' if tipe_tiket == '1' else 'VIP'}")
    print(f"Status Member: {'Ya' if status_member.lower() == 'y' else 'Tidak'}")
    print(f"Harga Dasar: Rp{harga_dasar:,.0f}")
    print(f"Diskon: {diskon*100:.0f}%")
    print(f"Harga Akhir: Rp{harga_akhir:,.0f}")

# Menjalankan program
if __name__ == "__main__":
    hitung_tiket()