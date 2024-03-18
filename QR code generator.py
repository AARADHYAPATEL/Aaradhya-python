import qrcode

data = "https://www.code.org/"
img = qrcode.make(data)
img.save("Code.png")
