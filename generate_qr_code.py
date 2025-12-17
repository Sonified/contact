#!/usr/bin/env python3
"""
Generate QR code for the contact page
"""

import qrcode
from pathlib import Path

# URL to encode
url = "http://contact.now.audio"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code (1 is smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (~30%)
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size in boxes
)

# Add data
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
output_path = Path(__file__).parent / "contact_qr_code.png"
img.save(output_path)

print(f"✓ QR code generated successfully!")
print(f"  URL: {url}")
print(f"  Saved to: {output_path}")
print(f"  Size: {img.size[0]}x{img.size[1]} pixels")
print()
print("Scan this QR code to visit the contact page!")
