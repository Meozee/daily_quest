while True:
    angka_1 = float(input("masukan angka pertama: "))
    operator = input("pilih operator (+,-,*, /): ")
    angka_2 = float(input("masukan angka kedua: "))

    # proses perhitungan
    if operator == "+":
        hasil = angka_1 + angka_2
        print(f"hasilnya adalah {hasil}")
    elif operator == "-":
        hasil = angka_1 - angka_2
        print(f"hasilnya adalah {hasil}")
    elif operator == "*":
        hasil = angka_1 * angka_2
        print(f"hasilnya adalah {hasil}")
    elif operator == "/":
        if angka_2 == 0:
            print("lu ga bisa mtk apa gimaan?")
        else:
            hasil = angka_1 / angka_2
            print(f"hasil pembagian ini adalah {hasil}")
    else:
        print("boe gelo budakteh!!!")

    # tanya lagi, mau lanjut?
    ulang = input("lagi ga? (ya/ga):").lower()
    if ulang == "ya":
        print ("oek kita lanjut lagi")
    else :
        print ("yausda")
        break


