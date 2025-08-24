import random

def main ():
    while True:
        print("SAMPURASUN MATE, LET'S GET GUESS")
        print("pilih dulu sesuai kemampuan ya jangan maksain nanti kealatan begonya")
        print("1 easy ∞ nyawa(buat bayi baru lahir si kalo kata gua mah)")
        print("2 normal 7 nyawa (warga +62)")
        print("3 angel poll 5 nyawa (cih kalo ga bisa ga usah maksa ya)")
        print("4 only king anu bisa iyeu mah 2 nyawa (mahkotamu menunggu di cakung)")
        print("5 kalo bisa lu langsung jadi DPR")

        pilihan = input("pilih sesuai keinginan  jangan kebutuhan:")

        if pilihan == "1":
            nyawa = None
        elif pilihan == "2":
            nyawa = 10
        elif pilihan == "3":
            nyawa = 6
        elif pilihan == "4":
            nyawa = 3
        elif pilihan == "5":
            nyawa = 1
        else:
            print ("pilih yang bener takut apa gimaan tuh?")
            continue

        angka_rahasia = random.randint(1,100)
        guess_times = 0

        print("\nGame beggin angkanya 1-100.\n")

        while True:
            try:
                tebakan = int(input("what is your answer king?:"))
                guess_times += 1

                if tebakan == angka_rahasia:
                    print(f"\n jir!!! angkanya {angka_rahasia} gg king kong rat")
                    print(f"dan lu butuh {guess_times} kali coba \n")
                    break
                else:
                    selisih = abs(tebakan - angka_rahasia)
                    presentase = 1 - (selisih / 100)

                    if tebakan < angka_rahasia:
                        if presentase >= 0.9:
                            print("tipis bet bos, up more")
                        elif presentase >= 0.75:
                            print("dikit lagi naik lagi bang")
                        elif presentase >= 0.47:
                            print("yu bisa yu")
                        elif presentase >= 0.35:
                            print("yu bisa yu")
                        elif presentase >= 0.2:
                            print ("NT jir")
                        else:
                            print("gelo budak teh nya")
                        
                    else:
                        if presentase >= 0.9:
                            print("tipis bet bos, bawah sikit")
                        elif presentase >= 0.75:
                            print("nih gua kasih tau bawah dikit bang")
                        elif presentase >= 0.47:
                            print("yu bisa yu")
                        elif presentase >= 0.35:
                            print("yu bisa yu")
                        elif presentase >= 0.2:
                            print ("NT jir")
                        else:
                            print("gelo budak teh nya")

                    if nyawa is not None:
                        nyawa -= 1
                        print(f"sisa nyawa: {nyawa}")
                        if nyawa <= 0:
                            print(f"\nyah, nyawaluh abis boba lagi dah kalo emang mental belom kena mah\n")
                            break

            except ValueError:
                print("ga penah SD apa gimana luh??")

        
        lagi = input("mau main lagi ga atau udah kena mental?(opsi jawa ban nya iya/ga:)").lower()
        if lagi == "iya":
            print ("\n----boleh juga king----\n")
        elif lagi == "ga":
           print("\nDIHH KENA MENTAL, CUPU\n")
        
           break


if __name__ == "__main__":
    main()