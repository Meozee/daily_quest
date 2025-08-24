#RETYPE THIS ONE TO REMEMBER
import math

def kalkulator_lanjutan():
    print("=== KALKULATOR PYTHON ===")
    print("Fitur yang tersedia:")
    print("1. Operasi dasar: +, -, *, /")
    print("2. Pangkat: ^")
    print("3. Akar kuadrat: sqrt")
    print("4. Sin, Cos, Tan (dalam derajat)")
    print("5. Logaritma: log")
    print("6. Konstanta: pi, e")
    print("7. Menggunakan hasil sebelumnya: ans")
    print("8. Bersihkan memori: clear")
    print("9. Keluar: exit")
    print("=" * 25)
    
    # Variabel untuk menyimpan hasil sebelumnya
    ans = 0
    history = []
    
    while True:
        try:
            # Input ekspresi matematika
            ekspresi = input("Masukkan ekspresi (atau 'help' untuk bantuan): ").strip().lower()
            
            # Keluar dari program
            if ekspresi == 'exit':
                print("Terima kasih telah menggunakan kalkulator!")
                break
                
            # Tampilkan bantuan
            if ekspresi == 'help':
                print("\nCara penggunaan:")
                print("- 5 + 3 (penjumlahan)")
                print("- 10 * 2 (perkalian)")
                print("- 4 ^ 2 (pangkat)")
                print("- sqrt(16) (akar kuadrat)")
                print("- sin(30) (sinus 30 derajat)")
                print("- log(100) (logaritma basis 10)")
                print("- pi (nilai π)")
                print("- ans (hasil sebelumnya)")
                print("- clear (hapus memori)")
                print("- history (lihat riwayat)")
                print("- exit (keluar)")
                print()
                continue
                
            # Tampilkan riwayat
            if ekspresi == 'history':
                if not history:
                    print("Riwayat kosong")
                else:
                    for i, h in enumerate(history, 1):
                        print(f"{i}. {h}")
                continue
                
            # Bersihkan memori
            if ekspresi == 'clear':
                ans = 0
                history = []
                print("Memori telah dibersihkan")
                continue
                
            # Ganti 'ans' dengan nilai hasil sebelumnya
            ekspresi = ekspresi.replace('ans', str(ans))
            
            # Ganti konstanta
            ekspresi = ekspresi.replace('pi', str(math.pi))
            ekspresi = ekspresi.replace('e', str(math.e))
            
            # Fungsi trigonometri (dalam derajat)
            if 'sin(' in ekspresi:
                start = ekspresi.find('sin(') + 4
                end = ekspresi.find(')', start)
                angle = float(ekspresi[start:end])
                result = math.sin(math.radians(angle))
                ekspresi = ekspresi[:start-4] + str(result) + ekspresi[end+1:]
                
            if 'cos(' in ekspresi:
                start = ekspresi.find('cos(') + 4
                end = ekspresi.find(')', start)
                angle = float(ekspresi[start:end])
                result = math.cos(math.radians(angle))
                ekspresi = ekspresi[:start-4] + str(result) + ekspresi[end+1:]
                
            if 'tan(' in ekspresi:
                start = ekspresi.find('tan(') + 4
                end = ekspresi.find(')', start)
                angle = float(ekspresi[start:end])
                result = math.tan(math.radians(angle))
                ekspresi = ekspresi[:start-4] + str(result) + ekspresi[end+1:]
                
            # Fungsi logaritma
            if 'log(' in ekspresi:
                start = ekspresi.find('log(') + 4
                end = ekspresi.find(')', start)
                num = float(ekspresi[start:end])
                result = math.log10(num)
                ekspresi = ekspresi[:start-4] + str(result) + ekspresi[end+1:]
                
            # Fungsi akar kuadrat
            if 'sqrt(' in ekspresi:
                start = ekspresi.find('sqrt(') + 5
                end = ekspresi.find(')', start)
                num = float(ekspresi[start:end])
                result = math.sqrt(num)
                ekspresi = ekspresi[:start-5] + str(result) + ekspresi[end+1:]
                
            # Ganti simbol pangkat
            ekspresi = ekspresi.replace('^', '**')
            
            # Evaluasi ekspresi
            hasil = eval(ekspresi)
            ans = hasil  # Simpan hasil untuk penggunaan berikutnya
            
            # Tambahkan ke riwayat
            history.append(f"{ekspresi} = {hasil}")
            
            # Tampilkan hasil
            print(f"Hasil: {hasil}")
            
        except ZeroDivisionError:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
        except ValueError:
            print("Error: Input tidak valid!")
        except Exception as e:
            print(f"Error: {e}")

# Jalankan kalkulator
kalkulator_lanjutan()