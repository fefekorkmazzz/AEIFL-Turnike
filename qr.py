import pandas as pd
import qrcode
import os

# 1. Excel dosyasını yükle
print("Excel dosyası yolunu yapıştırın")
excel_dosya = input()  # Excel dosyanızın adı

df = pd.read_excel(excel_dosya)

# 2. ID sütununun adını belirleyin (örnek: "ID" sütunu)
id_sutun_adi = "ID"  # Excel'deki sütun adı

# 3. QR kodları kaydetmek için klasör oluştur
kayit_klasoru = "qr_kodlar"
os.makedirs(kayit_klasoru, exist_ok=True)

# 4. Her ID için QR kod oluştur ve kaydet
for ogrenci_id in df[id_sutun_adi]:
    # QR kod üret
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(str(ogrenci_id))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Dosya adı: ID.png şeklinde
    dosya_yolu = os.path.join(kayit_klasoru, f"{ogrenci_id}.png")
    img.save(dosya_yolu)

print("✅ Tüm QR kodlar başarıyla oluşturuldu.")