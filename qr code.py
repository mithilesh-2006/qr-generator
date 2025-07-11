import qrcode
data = input("Enter http link to create QR : ")
name=input("Enter name to save file with png extention:")
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save(name)
print("QR Code generated and saved as",name)