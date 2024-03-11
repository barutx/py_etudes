#### FONSKSİYONLAR ODEV ####

### PROBLEM  1 
# def mukemmel_sayi(n):
#     muk = []
#     for i in range(1,n):
#         list_bolenler = [bol for bol in range(1,i) if i % bol == 0]
#         toplam = 0
#         for j in list_bolenler:
#             toplam += j
#         if toplam == i:
#             muk.append(i)
#     print(muk)

# mukemmel_sayi(10000)

## PROBLEM  2 

# def ebob_bul():
#     sayilar = input("İki sayı giriniz({},{}): ".format("x","y"))
#     x,y = map (int, sayilar.split(","))
#     bolenler= []
#     for i in range(1,(min(x,y)+1)):
#         if x % i == 0 and y % i == 0:
#             bolenler.append(i)
#     return max(bolenler)

# print(ebob_bul())

## PROBLEM 3 

# def ekok_bul():
#     sayilar = input("İki sayı giriniz({},{}): ".format("x","y"))
#     x,y = map(int,sayilar.split(","))
#     buyuk_sayi_katlari = []
#     for i in range(max(x,y),999999,max(x,y)):
#         buyuk_sayi_katlari.append(i)
#     for j in range(min(x,y),999999,min(x,y)):
#         if j in buyuk_sayi_katlari:
#             print(f"ekok({x},{y}) = {j}")
#             return j
#     print(f"ekok({x},{y})bulunumadı.")

# ekok_bul()

# PROBLEM 4

# def sayi_okunus():
#     sayi = int(input("İki basamaklı bir sayı giriniz: "))
#     ondalik = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
#     birlik = ["","bir", "iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

#     onda = sayi // 10
#     birde = sayi % 10
#     print(f"{ondalik[onda]}"+f"{birlik[birde]}")

# sayi_okunus()

# PROBLEM 5


# def pisagor_bul(n):
#     pisagor_degerleri=[]
#     for i in range(n+1):
#         for j in range(n+1):
#             for k in range(n+1):
#                 if i >j and i>k and (j**2 + k**2 == i**2):
#                     if (k,j,i) not in pisagor_degerleri:
#                         pisagor_degerleri.append((j,k,i))
#     print("Bu değerlerle pisagor üçgeni oluşturabilirsiniz: ", pisagor_degerleri, sep='\n')
                    
# pisagor_bul(100)


##### MODÜLLER ÖDEV


# import math
# # print(help(math))
# def help():
#     aciklama = """
#     ceil(x), comb(x,y), fabs(x), factorial(x), floor(x), fmod(x,y), gcd(x), isqrt(x), lcm(x), perm(x), exp2(x) fonksiyonlarını kullanabilirsiniz.
#     """
#     print(aciklama)


# def hesap_makinesi():
#     """math modülünündeki fonksiyonları kullanarak hesaplama yapmanızı sağlar.
#     ceil(x), comb(x,y), fabs(x), factorial(x), floor(x), fmod(x,y), gcd(x), isqrt(x), lcm(x), perm(x), exp2(x)
#     """

#     sayilar0 = ""
#     sayilar1 = ""
#     help()
#     fonk = input("Ne işlem yapmak istersiniz? ")

#     for i in fonk[fonk.index("("):-1]:
#         if i.isdigit():
#                 sayilar0 += i
#         elif i == ",":
#             for j in fonk[fonk.index(","):-1]:
#                 if j.isdigit():
#                     sayilar1 += j

#     deger0 = int(sayilar0)
#     if sayilar1 != "":
#         deger1 = int(sayilar1)

#     if "ceil" in fonk:
#         for i in range(int(deger0)):
#             print((math.ceil(i)* " ") + "*" + "--" + "*")
#         return math.ceil(deger0)
#     elif "comb" in fonk:
#         return math.comb(deger0, deger1)
#     elif "fabs" in fonk:
#         return math.fabs(deger0)
#     elif "factorial" in fonk:
#         print(f"{deger0}! = ", end="")
#         return math.factorial(deger0)
#     elif "floor" in fonk:
#         return math.floor(deger0)
#     elif "fmod" in fonk:
#         return math.fmod(deger0,deger1)
#     elif "gcd" in fonk:
#         return math.gcd(deger0)
#     elif "isqrt" in fonk:
#         return math.isqrt(deger0) 
#     elif "lcm" in fonk:
#         return math.lcm(deger0)
#     elif "perm" in fonk:
#         return math.perm(deger0)
#     elif "exp2" in fonk:
#         return math.exp2(deger0)

#     print(deger0)


# print(hesap_makinesi())





#### OOP ödev ####
