import qrcode
from io import BytesIO

def generate_qr_code(link, color):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color="white") # Use color variable
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer.getvalue() # Return base64 encoded image
