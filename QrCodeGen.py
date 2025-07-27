#generate a Qr code of my linkedin profile

from readline import backend

import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=4,)
# img=qr.make("https://www.linkedin.com/in/anuja-khatri-b39a22214/")
# img.save("Anuja_Khatri.png")

qr.add_data("https://www.linkedin.com/in/anuja-khatri-b39a22214/")
qr.make(fit=True)
img= qr.make_image(fill_color="blue", back_color="black")
img.save("anuja-khatri.png")
