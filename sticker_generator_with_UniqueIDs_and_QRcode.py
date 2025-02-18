import os
import argparse
import uuid
import qrcode
from PIL import Image, ImageDraw, ImageFont


ID_X = 37
ID_Y = 289
QR_X = 25
QR_Y = 362
fnt_sz = 38
fnt_clr = (211, 237, 234)

def generate_qrCode(unique_id):
    qr=qrcode.QRCode(version = 1, box_size=9, border=1)
    qr.add_data(unique_id)
    qr.make(fit=True)

    generated_qr = qr.make_image(fill_color="white", back_color="black")   
    return generated_qr

def generate_id():
    unique_id = str(uuid.uuid4())[0:8].upper()
    print(unique_id)
    return unique_id

def paste_to_template(unique_id, generated_qr):
    sticker = Image.open(args.sticker_template_path)
    #   pasting QR Code
    sticker.paste(generated_qr, (QR_X, QR_Y))               

    #   to paste ID on the sticker
    drawID = ImageDraw.Draw(sticker)    
    position = (ID_X, ID_Y)
    
    try:
        fnt = ImageFont.truetype('arial.ttf', fnt_sz)
    except IOError:
        try:
            fnt = ImageFont.truetype('DejaVuSans.ttf', fnt_sz)
        except IOError:
            fnt = ImageFont.load_default()
    drawID.text(position, unique_id, fill=fnt_clr, font=fnt)

    # Specifying output directory for generated stickers
    output_directory = 'D:/inventory_stickers_generator/2025_generated_stickers'
    if not os.path.exists(output_directory):
        print(f"Creating directory: {output_directory}")
        os.makedirs(output_directory)
    else:
        print(f"Directory already exists: {output_directory}")
    sticker.save(os.path.join(output_directory, f'{unique_id}.png'), dpi=(300,300))


parser = argparse.ArgumentParser(description="Generating easyD inventory stickers.")
parser.add_argument("count", type=int, help="Numbers of stickers. ")
parser.add_argument("sticker_template_path", type=str, help="The path to the sticker template. ")
args = parser.parse_args()


for no_of_stickers in range(args.count):
    unique_id = generate_id()
    generated_qr = generate_qrCode(unique_id)
    paste_to_template(unique_id, generated_qr)
    