import os
source_dir = "/home/gunner/Documents/Photo gallery stuff/ravensightgallery.github.io/images"

output_dir = os.getcwd()

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>
    body {{
      background: #111;
      color: #eee;
      font-family: sans-serif;
      padding: 20px;
      text-align: center;
    }}
    h1 {{
      margin-bottom: 20px;
    }}
    .gallery {{
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
    }}
    .gallery img {{
      width: 900px;
      max-width: 90%;
      border: 2px solid #444;
      border-radius: 8px;
      cursor: pointer;
      transition: transform 0.2s;
    }}
    .gallery img:hover {{
      transform: scale(1.05);
    }}
    .lightbox {{
      display: none;
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 9999;
      max-width: 90vw;
      max-height: 80vh;
      background: rgba(0, 0, 0, 0.9);
      padding: 10px;
      border-radius: 12px;
    }}
    .lightbox img {{
      max-width: 100%;
      max-height: 100%;
    }}
    .lightbox-close {{
      position: absolute;
      top: 5px;
      right: 10px;
      color: white;
      font-size: 24px;
      cursor: pointer;
    }}
    a {{
      color: #9ecbff;
      display: block;
      margin-top: 30px;
    }}
  </style>
  <script>
    function showLightbox(src) {{
      const box = document.getElementById('lightbox');
      const img = document.getElementById('lightbox-img');
      img.src = src;
      box.style.display = 'block';
    }}
    function closeLightbox() {{
      document.getElementById('lightbox').style.display = 'none';
    }}
  </script>
</head>
<body>
  <h1>{title}</h1>
  <div class="gallery">
    {images}
  </div>
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="" alt="Zoomed image">
  </div>
  <a href="index.html">← Back to Home</a>
</body>
</html>
"""

for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        images_html = ""
        for file in sorted(os.listdir(folder_path)):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                rel_path = os.path.relpath(os.path.join(folder_path, file), output_dir)
                images_html += f'<img src="{rel_path}" alt="{file}" onclick="showLightbox(\'{rel_path}\')">\n'

        page_name = folder.replace(" ", "-") + ".html"
        output_path = os.path.join(output_dir, page_name)

        with open(output_path, "w") as f:
            f.write(html_template.format(title=folder, images=images_html))

print("✅ Gallery pages generated.")
