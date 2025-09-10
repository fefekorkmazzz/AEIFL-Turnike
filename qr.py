import pandas as pd
import qrcode
import os

print("Excel dosyası yolunu yapıştırın")
excel_dosya = input()  # Excel dosyanızın adı

print("QR kodların kaydedileceği dosya yolunu yapıştırın")
kayit_klasoru = input()

df = pd.read_excel(excel_dosya)


id_sutun_adi = "ID"  # Excel'deki sütun adı



os.makedirs(kayit_klasoru, exist_ok=True)


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