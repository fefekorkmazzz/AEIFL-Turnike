import pandas as pd
import qrcode
import os

print("Excel dosyası yolunu yapıştırın")
excel_dosya = input()

print("QR kodların kaydedileceği dosya yolunu yapıştırın")
kayit_klasoru = "F:\\PROJELER\\Yemekhane\\qr_kodlar"

# Excel dosyasını oku, sütun adlarını otomatik ver
df = pd.read_excel(excel_dosya, header=None)

# 2. satırdan itibaren veri var, 1. satır boş
df = df.iloc[1:]  # 0-indexli olduğu için 1'den başlıyoruz

# Sütun indeksleri: 0 = İsim, 1 = Soyad, 2 = ID
isim_index = 0
soyad_index = 1
id_index = 2

os.makedirs(kayit_klasoru, exist_ok=True)

for _, row in df.iterrows():
    isim = str(row[isim_index]).strip()
    soyad = str(row[soyad_index]).strip()
    ogrenci_id = str(row[id_index]).strip()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(ogrenci_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    dosya_adi = f"{isim}_{soyad}.png".replace(" ", "_")
    dosya_yolu = os.path.join(kayit_klasoru, dosya_adi)
    img.save(dosya_yolu)

print("✅ Tüm QR kodlar başarıyla oluşturuldu.")
