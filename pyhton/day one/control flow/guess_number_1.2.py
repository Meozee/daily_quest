#retype this one
import random

def dapatkan_selisih_persen(tebakan, angka_rahasia):
    """Menghitung seberapa dekat tebakan dalam persentase"""
    if angka_rahasia == 0:
        return 100  # Hindari pembagian 0
    selisih = abs(tebakan - angka_rahasia)
    persen = (selisih / angka_rahasia) * 100
    return persen

def dapatkan_petunjuk(tebakan, angka_rahasia):
    persen = dapatkan_selisih_persen(tebakan, angka_rahasia)
    selisih = angka_rahasia - tebakan

    if persen < 10:  # Kurang dari 10% selisih → hampir tepat
        if selisih > 0:
            return "Dikit banget lagi kekecilan! Hampir tepat!"
        else:
            return "Dikit banget lagi kegedean! Nyaris!"
    elif persen < 25:
        if selisih > 0:
            return "Masih kekecilan, tapi udah deket!"
        else:
            return "Masih kegedean, tapi udah deket!"
    elif persen < 50:
        if selisih > 0:
            return "Masih terlalu kecil, tapi mendingan!"
        else:
            return "Masih terlalu gede, tapi mendingan!"
    else:
        if selisih > 0:
            return "Jauh banget, kekecilan atuh!"
        else:
            return "Jauh banget, kegedean bro!"

def main():
    print("="*50)
    print("🎮 SELAMAT DATANG DI GAME TEBAK ANGKA 🔢")
    print("Ukuran apa tuh man? Ukuran ukirin wkwk")
    print("="*50)

    while True:
        # Menu pilihan mode
        print("\n🔥 PILIH MODE:")
        print("1. Easy (Tak terbatas nyawa - tapi jangan harap gampang)")
        print("2. Normal (7 nyawa)")
        print("3. Hard (5 nyawa)")
        print("4. Extreme (2 nyawa)")
        print("5. Dewa Mode (1 tebakan - sekali mati, sekali hidup)")

        try:
            pilihan = int(input("Pilih mode (1-5): "))
            if pilihan == 1:
                nyawa = float('inf')  # Tak terbatas
                mode = "Easy"
            elif pilihan == 2:
                nyawa = 7
                mode = "Normal"
            elif pilihan == 3:
                nyawa = 5
                mode = "Hard"
            elif pilihan == 4:
                nyawa = 2
                mode = "Extreme"
            elif pilihan == 5:
                nyawa = 1
                mode = "Dewa Mode"
            else:
                print("Pilih angka 1-5 ya man!")
                continue
        except ValueError:
            print("Masukin angka yang bener lah!")
            continue

        print(f"\n🔥 Mode: {mode} | Nyawa: {'∞' if nyawa == float('inf') else nyawa}")
        print("Aku lagi mikir angka antara 1 sampai 100...")

        angka_rahasia = random.randint(1, 100)
        guess_times = 0
        main_lagi = False

        while nyawa > 0:
            try:
                tebakan = int(input(f"\n👉 Tebak angkanya ({'∞' if nyawa == float('inf') else nyawa} nyawa tersisa): "))
                guess_times += 1

                if tebakan < 1 or tebakan > 100:
                    print("Masukin angka 1-100 lah, jangan aneh-aneh!")
                    continue

                if tebakan == angka_rahasia:
                    print(f"🎯 JIR BENER CO! Angkanya memang {angka_rahasia}!")
                    print(f"🏆 Kamu menang dalam {guess_times} kali tebak! Mode: {mode}")
                    break
                else:
                    # Beri petunjuk berdasarkan persentase
                    petunjuk = dapatkan_petunjuk(tebakan, angka_rahasia)
                    if tebakan < angka_rahasia:
                        print(f"⬆️  {petunjuk} (kekecilan atuh kaya punya lu)")
                    else:
                        print(f"⬇️  {petunjuk} (kegedena bang kaya punya gua)")

                    if nyawa != float('inf'):  # Kurangi nyawa jika bukan mode easy
                        nyawa -= 1

            except ValueError:
                print("Masukin angka dong, bukan huruf atau simbol aneh!")
                continue

        else:
            # Kalah karena kehabisan nyawa
            print(f"💀 NYAWA HABIS! Angka yang benar adalah {angka_rahasia}")
            if mode == "Dewa Mode":
                print("Dewa aja salah, apalagi lu wkwk")

        # Tanya main lagi
        while True:
            ulang = input("\n>Main lagi? (y/n): ").lower().strip()
            if ulang in ['y', 'yes', 'ya', 'iya']:
                break
            elif ulang in ['n', 'no', 'tidak']:
                print("Oke! Makasih udah main. Jaga jodoh ya!")
                return  # Keluar dari program
            else:
                print("Masukin 'y' atau 'n' aja lah.")

# Jalankan game
if __name__ == "__main__":
    main()