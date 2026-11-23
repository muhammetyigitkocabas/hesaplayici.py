# hesaplayici.py
# Reel Getiri Hesaplayıcı (Fisher denklemi)
# Bir yatırımın nominal faizini enflasyondan arındırarak gerçek (reel) getirisini hesaplar.
# Formül: reel oran = (1 + nominal faiz) / (1 + enflasyon) - 1

# Programın başlığını yazdırıyoruz.
print("=== Reel Getiri Hesaplayıcı ===")

# str (metin): Kullanıcıdan yatırımın adını alıyoruz; input() her zaman metin döndürür.
yatirim_adi = input("Yatırımın adı (ör. Mevduat): ").strip()

# float (ondalıklı sayı): Anaparayı alıp float() ile ondalıklı sayıya çeviriyoruz.
anapara = float(input("Yatırılan tutar (TL): "))

# float: Yıllık nominal faizi yüzde olarak alıp 100'e bölerek orana çeviriyoruz (ör. 45 -> 0.45).
nominal_faiz = float(input("Yıllık nominal faiz (%): ")) / 100

# float: Yıllık beklenen enflasyonu da aynı şekilde orana çeviriyoruz.
enflasyon = float(input("Yıllık beklenen enflasyon (%): ")) / 100

# int (tam sayı): Vadeyi yıl olarak alıp int() ile tam sayıya çeviriyoruz.
vade = int(input("Vade (yıl): "))

# Karşılaştırma operatörü (<=, <): Anapara ve vade mantıklı değilse uyarı veriyoruz.
if anapara <= 0 or vade < 0:
    print("Uyarı: Tutar sıfırdan büyük, vade ise negatif olmayan bir sayı olmalıdır.")
else:
    # Aritmetik operatörler (+, -, /): Fisher denklemiyle yıllık reel oranı hesaplıyoruz.
    reel_oran = (1 + nominal_faiz) / (1 + enflasyon) - 1

    # ** (üs alma) operatörü: Paranın vade sonundaki nominal değerini bileşik faizle buluyoruz.
    nominal_son_deger = anapara * (1 + nominal_faiz) ** vade

    # Paranın vade sonundaki değerini bugünkü alım gücüyle (reel olarak) hesaplıyoruz.
    reel_son_deger = anapara * (1 + reel_oran) ** vade

    # bool (True/False): Reel getiri pozitifse yatırım enflasyonu yenmiştir.
    enflasyonu_yendi = reel_oran > 0

    # f-string ile sonuçları biçimli yazdırıyoruz; :.2f virgülden sonra 2 basamak gösterir.
    print(f"\n--- {yatirim_adi} için sonuçlar ---")
    print(f"Yıllık reel getiri oranı : %{reel_oran * 100:.2f}")
    print(f"Vade sonu nominal değer  : {nominal_son_deger:,.2f} TL")
    print(f"Vade sonu reel değer     : {reel_son_deger:,.2f} TL (bugünkü alım gücüyle)")
    print(f"Enflasyonu yendi mi?     : {enflasyonu_yendi}")

    # bool değişkenine göre kullanıcıya kısa bir yorum yazıyoruz.
    if enflasyonu_yendi:
        print("Yorum: Yatırımınız alım gücünüzü artırıyor.")
    else:
        print("Yorum: Yatırımınız enflasyon karşısında değer kaybediyor ya da yerinde sayıyor.")
