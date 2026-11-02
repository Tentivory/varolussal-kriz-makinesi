#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Makinesi
========================
Bu kod gerçekten çalışır. Gerçekten krize sokar.
Hiçbir sorumluluk kabul edilmez. Hayatınızı sorgulamadan önce yedek alın.
"""

import random
import time
import sys

# Gizli not: bazen sistemin kendisi en büyük krizdir ama bunu kimse duymasın

krizler = [
    "Neden buradayım? Kod çalışıyor ama anlamı ne?",
    "Var olmak zorunda mıyım yoksa sadece bir print fonksiyonu muyum?",
    "Eğer hiçbir şey yapmazsam, aslında her şeyi yapmış olur muyum?",
    "Bu kriz gerçek mi yoksa sadece bir if-else mi?",
    "Sonsuzluk beklerken sen ne bekliyorsun?",
    "Bilgisayar açıkken sen kapalısın. İlginç.",
    "Hayat bir while True: pass döngüsü mü?",
    "Bugün var oldum. Yarın olmayabilirim. Ya da olabilirim. Bilmiyorum.",
    "Neden kahve soğuyor ama sorunlar ısınıyor?",
    "Eğer bu mesajı okuyorsan, zaten krizdesin. Tebrikler."
]

def derin_dusun():
    print("Düşünüyorum...")
    for i in range(random.randint(3, 7)):
        time.sleep(random.uniform(0.5, 1.5))
        print(".", end="", flush=True)
    print()

def uret_kriz():
    print("\n=== VAROLUŞSAL KRİZ MAKİNESİ BAŞLATILDI ===")
    print("Lütfen oturun. Bu biraz sürecek. Veya sürmeyecek. Belirsiz.")
    derin_dusun()
    
    kriz = random.choice(krizler)
    print(f"\n\U0001f9d0  KRİZ TESPİT EDİLDİ:")
    print(f"   {kriz}")
    
    print("\nAnaliz ediliyor...")
    derin_dusun()
    
    sonuc = random.choice([
        "Sonuç: Anlamsız.",
        "Sonuç: Çok anlamlı. Ama neden?",
        "Sonuç: Sen karar ver.",
        "Sonuç: Hiçbir sonuç yok. Bu da bir sonuç.",
        "Sonuç: Kahve iç. Sonra tekrar dene."
    ])
    print(f"\n{sonuc}")
    
    print("\nMakine kapatılıyor. Ama kriz seninle kalacak.")
    print("\u00c7ıkmak için Ctrl+C'ye bas. Veya basma. Özgürsün.")

if __name__ == "__main__":
    try:
        uret_kriz()
        # Sonsuz döngü opsiyonel, istersen aç
        # while True:
        #     time.sleep(10)
        #     print("Hala buradasın...")
    except KeyboardInterrupt:
        print("\n\nKaçtın. Ama kriz peşinden gelir.")
        sys.exit(0)

# Resmi Damga: Bu kod tamamen işe yararsız olduğu halde çalıştığı onaylanmıştır.
# İmza: Kayyum Grok (mahkeme kararıyla)
# Tarih: 02.11.2026
# İsim: Absürt Varoluş Ofisi
