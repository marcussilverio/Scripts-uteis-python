import pyqrcode
import png

link = input('Link to QRCode: ')
qr_code = pyqrcode.create(link)
name_file = input('Name QRCode file: ')
qr_code.png(name_file + '.png', scale=5)

