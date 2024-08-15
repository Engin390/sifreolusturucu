import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifreniz kaç karakterden oluşsun?"))


password = ""
for i in range(sayi):
    password += random.choice(karakterler)


print("Şifreniz:", password)

while True:
    if sayi==0:
        print("geçersiz.")
