import os
from PIL import ExifTags

# Fix image orientation based on EXIF metadata
def correct_orientation(img):
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = img._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation, None)
            if orientation_value == 3:
                img = img.rotate(180, expand=True)
            elif orientation_value == 6:
                img = img.rotate(270, expand=True)
            elif orientation_value == 8:
                img = img.rotate(90, expand=True)
    except Exception as e:
        print(f"⚠️ EXIF orientation fix failed: {e}")
    return img

from PIL import Image, ImageDraw, ImageFont, ImageOps

base_dir = "gallery_images"
watermark_text = "© RavenSightGallery"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # fallback font

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if not os.path.isdir(folder_path):
        continue

    print(f"\n📂 Processing: {folder}")

    watermarked_dir = os.path.join(folder_path, "watermarked")
    os.makedirs(watermarked_dir, exist_ok=True)

for filename in sorted(os.listdir(folder_path)):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        src_path = os.path.join(folder_path, filename)
        dest_path = os.path.join(watermarked_dir, filename)

        img = Image.open(src_path)
        img = ImageOps.exif_transpose(img)  # Fix orientation based on EXIF

        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype(font_path, size=int(img.height * 0.03))
        except:
            font = ImageFont.load_default()

        text_width, text_height = draw.textsize(watermark_text, font=font)
        position = (img.width - text_width - 20, img.height - text_height - 20)

        draw.text(position, watermark_text, font=font, fill=(255, 255, 255, 180))
        img.save(dest_path)

        print(f"✅ Watermarked: {filename}")
