# This mini-project is a QR Code Generator developed using Python. It utilizes the qrcode library to create a QR code for a given URL or text and employs Pillow (PIL) for image processing and saving. The script allows customization of QR code size, error correction levels, and colors, making it adaptable for various applications such as website links, digital payments, and business cards. This project serves as a practical implementation of QR code technology, offering a simple yet effective solution for quick data sharing.





import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://www.wscubetech.com/")
qr.make(fit=True)

# Correct spelling of fill_color and back_color
img = qr.make_image(fill_color="red", back_color="white")

# Save the QR code image
img.save("wscubetech.png")

print("QR Code generated successfully!")
