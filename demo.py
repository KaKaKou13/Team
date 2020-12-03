import pyqrcode

from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Bike Lock")
qr.png("BikeLock.png", scale=8)
