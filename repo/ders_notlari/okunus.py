def okunus_ile_okunus_belirle(sayi):
    okunus = ''
    birler = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
    onlar = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]

    if sayi < 10:
        okunus = birler[sayi]
    elif sayi < 100:
        birler_basamagi = sayi % 10
        onlar_basamagi = sayi // 10    ## sayi parametresini koymamız gerekmiyor mu?
        okunus = onlar[onlar_basamagi]
        if birler_basamagi != 0:
            okunus += birler[birler_basamagi]
    else:
        okunus = "Hata: 0 ile 99 arasında bir sayı giriniz."

    print(okunus)
    print(okunus[-3:])

    if 'ü' in okunus[-3:]:  #### bunu 'tür yapabiliriz
        return 'tür'
    elif 'i' in okunus[-3:]: 
        if 'ş' in okunus[-3:]:  #  yetmiş 'tir'
            return 'tir'       
        return 'dir'   
    elif 'ı' in okunus[-3:]:
        if 'ş' or 'k' in okunus[-3:]: #kırk, altmış
            return 'tır'
        return 'dır'
    elif 'u' in okunus[-3:]:
        return 'dur'
    else:  ## beş
        return 'tir'
   
    

sayi = int(input("Lütfen bir sayı girin: "))
print(f"Sayı = {sayi}'{okunus_ile_okunus_belirle(sayi)}") ## kesme işareti 