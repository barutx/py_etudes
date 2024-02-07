### PROBLEM 1 ###
# def main():
#     numbers = [int(input(f"What's {var}? ")) for var in ['x','y','z']]

#     print(numbers[0]*numbers[1]*numbers[2])

# main()

#### PROBLEM 2 ####

# def main():
#     endeks = [int(input(f"{var} nedir? ")) for var in ["Kilonuz","Boyunuz"]]
#     kilo = float(endeks[0])
#     boy = float(endeks[1])
#     beden_kitle_endeksi = kilo/boy**2
#     print(f"Sonuç :{beden_kitle_endeksi:.5f}")
# main()


#### PROBLEM 3 ####

# def main():
#     x = float(input("Aracınız kilometrede kaç litre benzin yakıyor?: {}lt: ".format(0)))
#     y = float(input("Kaç kilometre yol yaptınız?: {}km: ".format(0)))

#     harcanan_benzin = x*y
    
#     litre_fiyat = 39.35  ## HOW TO GET ACTUAL PRICE ?
#     result = harcanan_benzin*litre_fiyat 
#     print(f"Toplam borcunuz: {result:.2f} TL")
# if __name__ =="__main__":
#     main()

### PROBLEM 4 ####
# def main():
#     bilgiler = [input(f"{i} nedir? ") for i in ['Adınız','Soyadınız', "Telefon numaranız"]]
#     ad = bilgiler[0]
#     soyad = bilgiler[1]
#     numara = bilgiler[2]

#     print(ad,soyad,numara, sep="\n")
# if __name__ == '__main__':
#     main()

### PROBLEM 5 ####
# def main():
#     numbers = [int(input(f"Give me the {var} number: "))for var in ['first', 'second']]

#     a = numbers[0]
#     b = numbers[1]
#     a,b = b,a
#     print(a,b)
# if __name__ == '__main__':
#     main()

#### PROBLEM 6 ####

def root(n):
    epsilon = 0.00001
    low = 0
    high = n
    guess = (high+low)/2
    while abs(guess**2-n) >= epsilon:
        if guess**2 > n:
            high=guess
        elif guess**2 < n:
            low=guess
        else:
            break
        guess = (high+low)/2  ### If not, loop goes to infinity       
    if abs(guess**2-n) <= epsilon:
        return guess
    else: 
        return None


try:
    kenarlar = [int(input(f"{var} kenar uzunluğu: ")) for var in ['Birinci','İkinci']]
    a = kenarlar[0]
    b = kenarlar[1]
    c_kare = a**2 + b**2
    hipotenüs = root(c_kare)
    print(f"Hipotenüs: {hipotenüs:.6f}")
    pass
except (TypeError, ValueError):
    pass


