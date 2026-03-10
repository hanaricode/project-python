def tampilkan_menu():
    
    """Menampilkan menu kalkulator"""
    
    print("\n" + "="*30)
    print("     KALKULATOR SEDERHANA")
    print("="*30)
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    print("="*30)

def operasi(number):         # Meminta input angka dari user menggunakan try-except untuk menangani input non-angka
    while True:
        try:
            angka = float(input(number))
            return angka
        except ValueError:
            print("Error: Input harus angka! Silakan coba lagi.")

def penjumlahan():
    """Operasi penjumlahan"""
    print("\n-- Penjumlahan --")
    angka1 = operasi("Masukkan angka pertama: ")
    angka2 = operasi("Masukkan angka kedua: ")
    hasil = angka1 + angka2
    print(f"Hasil Perhitungan: {angka1} + {angka2} = {hasil}")

def pengurangan():
    """Operasi pengurangan"""
    print("\n-- Pengurangan --")
    angka1 = operasi("Masukkan angka pertama: ")
    angka2 = operasi("Masukkan angka kedua: ")
    hasil = angka1 - angka2
    print(f"Hasil Perhitungan: {angka1} - {angka2} = {hasil}")

def perkalian():
    """Operasi perkalian"""
    print("\n-- Perkalian --")
    angka1 = operasi("Masukkan angka pertama: ")
    angka2 = operasi("Masukkan angka kedua: ")
    hasil = angka1 * angka2
    print(f"Hasil Perhitungan: {angka1} x {angka2} = {hasil}")

def pembagian():      # Menggunakan try-except untuk menangani pembagian dengan nol
    
    print("\n-- Pembagian --")
    angka1 = operasi("Masukkan angka pertama: ")
    
    while True:       # Loop terus sampai user memasukkan angka selain nol
        try:
            angka2 = operasi("Masukkan angka kedua: ")
            if angka2 == 0:
                print("Error: Operasi pembagian tidak bisa dibagi dengan nol! Silakan input angka selain nol.")
                continue
            hasil = angka1 / angka2
            print(f"Hasil Perhitungan: {angka1} ÷ {angka2} = {hasil}")
            break
        except Exception as e:
            print(f"Error: Terjadi kesalahan - {e}")

def main():       # Fungsi utama program kalkulator

    while True:
        try:
            tampilkan_menu()
            pilihan = input("Pilih operasi (1-5): ").strip()
            
            # Pemilihan operasi
            if pilihan == '1':
                penjumlahan()
            elif pilihan == '2':
                pengurangan()
            elif pilihan == '3':
                perkalian()
            elif pilihan == '4':
                pembagian()
            elif pilihan == '5':
                print("Program selesai!")
                break
            else:
                print("Error: Pilihan tidak ada! Silakan pilih antara 1-5.")
                
        except KeyboardInterrupt:
            print("\nProgram dihentikan oleh user.")
            print("Terima kasih!")
            break
        except Exception as f:
            print(f"Terjadi kesalahan tak terduga: {f}")
            print("Program akan berjalan")

if __name__ == "__main__":
    main()