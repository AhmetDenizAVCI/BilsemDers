print("""HESAP MAKİNESİ
1- TOPLAMA
2- ÇIKARMA
3- ÇARPMA
4- BÖLME
Lütfen bir seçim yapınız
Çıkmak için \"çıkış\" yazınız""" ) # \ ile sonraki karakteri görme dedik, böylece çift tırnak kullanabildik

islem=input("Seçiminiz: (1-4)") #dikkat, int e çevirmedim! acaba if de nasıl kullanılacak?

sayi1=int(input("Birinci sayıyı giriniz:")) #inputtan gelen deger string turunde oldugu için int e çevirdim
sayi2=int(input("İkinci sayıyı giriniz:"))

if islem=="1":
    print(sayi1 + sayi2)
elif islem=="2":
    print(sayi1 - sayi2)
elif islem=="3":
    print(sayi1 * sayi2)
elif islem=="4":
    print(sayi1 / sayi2)
elif islem=="çıkış":
    print("Hoşçakal...")
else:
    print("Hatalı seçim!")