import random
sayi = random.randint(0, 101)
chance = 5
while chance > 0:
    tahmin = int(input("Hadi Pozitif bir sayı girde Başlayalım: "))
    if tahmin < 0:
        print("Girdiğiniz Değer Pozitif Bir Tmsayı değil Lütfen pozitif bir sayı giriniz")
        continue
    chance -= 1
    if sayi > tahmin:
        print("Yukarı Kalan Hakkınız {}".format(chance))
    elif sayi < tahmin:
        print("Aşağı Kalan Hakkınız {}".format(chance))
    else:
        print("Doğru Tahmin Ettiniz Tebrikler")
        break
    if chance == 0:
        print("Bilemedin ajkfhjklsdhjdfklshjklafahjkdfshjkladfs Sayımız {}".format(sayi))
