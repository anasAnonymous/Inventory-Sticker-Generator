# Inventory Stickers Generator
This is a Python program to generate inventory stickers with a unique ID and a QR code. The generated stickers are saved as images.

## Features
- Generates a unique ID for each sticker.
- Creates a QR code for the unique ID.
- Adds the unique ID and QR code to a sticker template.
- Saves the generated sticker images in a specified folder.

## Prerequisites
Make sure you have Python installed on your system. You also need to install some required libraries.

### Install Required Libraries

Use the following command to install the required Python libraries:

```bash
pip install qrcode[pil] pillow argparse
```

## How to Run the Program
- Open the command prompt or terminal.
- Go to the folder where the script is saved.
- Run the script using the following command:

```bash
program_name.py <number_of_stickers> <sticker_template_path>
