#kullanıcı adı admin parola 123456
print("Hoşgeldiniz")
kullaniciadi=input("Lütfen Kullanıcı adını girin:")
if  kullaniciadi==("admin") :
    print("Kullanıcı adı doğru.")
    sifre=input("Şifrenizi giriniz:")
    if sifre==("123456"):
        print("Şifre doğru, hoşgeldiniz")
    else :
        print("Şifre yanlış, lütfen tekrar deneyiniz")
else :
    print("Kullanıcı adı yanlış")