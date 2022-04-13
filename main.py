import qrcode

x = str(input("URL => "))

qr = qrcode.make(x)
qr.save("QRCODE.png")