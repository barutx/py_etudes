
#### KOŞULLU DURUMLAR

## PROBLEM 1

# veriler = [float(input(f"{veri} giriniz:")) for veri in ['Kilonuzu', 'Boyunuzu(m)']]
# kilo, boy = veriler[0], veriler[1]

# indeks = kilo / boy**2
# print(f"Beden Kitle İndeksi:{indeks:.3f}", end =' ')
# if indeks < 18.5: 
#     print('Zayıf')
# elif  18.5 <= indeks < 25:
#     print('Normal')
# elif 25 <= indeks < 30:
#     print("Fazla Kilolu")
# else:
#     print('Obez')


## PROBLEM 2 
# sayilar = [int(input(f"{var}. sayıyı giriniz: "))for var in range(1,4)]
# print(max(sayilar))


## PROBLEM 3 
# vize1 = int(input('Birinci vize notunuz: '))
# vize2= int(input('İkinci vize notunuz: '))
# final = int(input("Final sınavı notunuz: "))

# total = (3/10*vize1) + (3/10*vize2) + (4/10*final)
# print(total, end=" ")
# if total >= 90:
#     print("AA")
# elif total >= 85:
#     print("BA")
# elif total >= 80:
#     print("BB")
# elif total >= 75:
#     print("CB")
# elif total >= 70:
#     print("CC")
# elif total >= 65:
#     print("DC")
# elif total >= 60:
#     print("DD")
# elif total >= 55:
#     print('FD')
# else: 
#     print('FF')


# PROBLEM 4
# while True:
#         try:
#             sekil = input("Dörtgen mi üçgen mi bulmak istersiniz?(dörtgen/üçgen): ")
#             if sekil == 'dörtgen':
#                 while True:
#                     try:
#                         kenarlar = [int(input(f"{var}. kenar: ")) for var in range(1,5)]
#                         if kenarlar.count(max(kenarlar)) == 2 and kenarlar.count(min(kenarlar)) == 2:
#                             print('Bu bir dikdörtgendir')
#                             break
#                         elif kenarlar.count(max(kenarlar)) == 4:
#                             print('Bu bir karedir.')
#                             break
#                         else:
#                             print('Bu bir dörtgendir.') 
#                             break   
#                     except (TypeError, ValueError):
#                         print("Bu bir tamsayı değil, tekrar deneyiniz.")
#                         continue  
#                 break                                             
#             elif sekil == 'üçgen':
#                 while True:
#                     try:
#                         kenarlar = [int(input(f"{var}. kenar: ")) for var in range(1,4)]
#                         a = abs(kenarlar[0]-kenarlar[2]) < kenarlar[1] < (kenarlar[0] + kenarlar[2])
#                         b = abs(kenarlar[1]-kenarlar[2]) < kenarlar[0] < (kenarlar[1] + kenarlar[2])
#                         c = abs(kenarlar[0]-kenarlar[1])< kenarlar[2]< (kenarlar[0]+kenarlar[2])
#                         if a and b and c:
#                             print("Bu bir üçgendir")
#                             break
#                         else:
#                             print("Bu değerlerle bir üçgen oluşturmak mümkün değil.")
#                             continue  
#                     except(TypeError,ValueError):
#                         print("Bu bir tamsayı değil, tekrar deneyiniz.")
#                         continue
#                 break                  
#             else:
#                 print("Verdiğiniz değer bir geometrik şekil ile ölçüşmüyor.")              
#         except(TypeError, ValueError):
#                 continue

##### DÖNGÜLER

## PROBLEM 1 
# sayi = int(input("Bir sayı giriniz: "))

# bolenler_toplami =0
# for i in range(1,sayi):
#     if sayi % i == 0:
#         bolenler_toplami += i
# if bolenler_toplami == sayi:
#     print(f"{sayi} bir mükemmel sayıdır.")
# else:
#     print(f"{sayi} bir mükemmel sayı değildir.")


#### PROBLEM 2 
# sayi = input("Bir sayı giriniz: ")
# basamaklar = list(sayi)
# toplam = 0
# for i in basamaklar:
#     toplam += int(i)**len(sayi)
# if toplam == int(sayi):
#     print(f"{sayi} bir Armstrong sayısıdır.")
# else:
#     print(f"{sayi} bir Armstrong sayısı değildir.")

## PROBLEM 3 

# for i in range(1,10):
#     for j in range(1,10):
#         print(i,j, sep='*',end=" ")
#         print('=',i*j)

### PROBLEM 4 

# toplam = 0
# while True:
#     try:
#         sayi = input("Bir sayı giriniz: ")
#         if sayi != 'q':
#             toplam += int(sayi)
#         elif sayi == 'q':
#             print(f"Toplam: {toplam}")
#             break
#     except (ValueError,TypeError):
#         print("Bu bir sayı değil.")
        

# PROBLEM 5
for i in range(1,100):
    if i % 3 == 0:
        print(i, end=" ")    ### EN SONDA % ÇIKIYOR NEDEN ACABA?
    else:
        continue
        

#PROBLEM 6

# cift_sayilar = [i for i in range(1,100) if i % 2 == 0]
# print(cift_sayilar)





                
