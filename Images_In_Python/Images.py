"""
This script demonstrates how to work with images in Python using the Pillow library.

What is Pillow?
---------------
Pillow is a popular Python library used for opening, manipulating, and saving image files.
It's often the first result when searching for how to work with images in Python.

To install:
    pip install pillow

Main Features Demonstrated:
- Opening and displaying an image
- Accessing image properties (size, format, mode)
- Image transformations (rotate, crop, paste, save)
- Pixel-level editing (changing color of specific pixels)
"""

from PIL import Image

# Load an image file (replace with a valid path to your image)
img = Image.open("your_image.jpg")  # <- replace with your image file

# Display image information
print("📏 Size:", img.size)
print("🖼️ Format:", img.format)
print("🎨 Mode:", img.mode)

# Show the image
img.show()

# --- Image Transformations ---

# Rotate the image by 180 degrees
rotated_img = img.rotate(180)
rotated_img.save("rotated_image.jpg")

# Crop a region (left, upper, right, lower)
cropped_img = img.crop((100, 100, 400, 400))
cropped_img.save("cropped_image.jpg")

# Paste cropped image into original
pasted_img = img.copy()
pasted_img.paste(cropped_img, (0, 0))
pasted_img.save("pasted_image.jpg")

# --- Pixel-level Editing ---

# Change a single pixel to red at (100, 100)
img.putpixel((100, 100), (255, 0, 0))

# Change a 10x10 block of pixels to blue
for i in range(10):
    for j in range(10):
        img.putpixel((150 + i, 150 + j), (0, 0, 255))

# Optionally adjust transparency (if supported by image mode)
if img.mode in ("RGBA", "LA"):
    img.putalpha(25)

# Save the modified image
img.save("modified_image.jpg")
