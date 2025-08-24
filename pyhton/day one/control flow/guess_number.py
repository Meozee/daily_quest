import random

angka_rahasia = random.randint (1,100)
guess_times = 0 

print("selaamt datang di game tebak ukuran")
print("ukuran apa tuh man")
print ("ukuran ukirin")

while True :
    try:
        tebakan = int(input("sini ayo tebak:"))
        guess_times += 1

        if tebakan < angka_rahasia:
            print ("kekecilan atuh kaya punya lu")
        elif tebakan > angka_rahasia:
            print("kegedena bang kaya punya gua")
        else:
            print(f"jir bener co {angka_rahasia}")
            break
    except ValueError:
        print ("yang bener lah, angka dong yang harusnya lu masukin")
