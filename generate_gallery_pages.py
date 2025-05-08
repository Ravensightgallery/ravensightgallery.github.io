import os

source_dir = "gallery_images"
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
      width: 300px;
      max-width: 100%;
      height: auto;
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
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.95);
      justify-content: center;
      align-items: center;
      flex-direction: column;
      z-index: 9999;
    }}
    .lightbox img {{
      max-width: 90%;
      max-height: 90%;
    }}
    .lightbox-close {{
      position: absolute;
      top: 10px;
      right: 20px;
      color: white;
      font-size: 24px;
      cursor: pointer;
    }}
  </style>
</head>
<body>
  <h1>{title}</h1>
  <div class="gallery">
    {images}
  </div>
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <span class="lightbox-close">&times;</span>
    <img id="lightbox-img" src="" alt="">
    <div id="lightbox-caption" style="color:white; margin-top:10px;"></div>
  </div>
  <br><a href="index.html">← Back to Home</a>
  <script>
    let images = [];
    let currentIndex = -1;

    function showLightbox(src) {{
      images = Array.from(document.querySelectorAll('.gallery img'));
      currentIndex = images.findIndex(img => img.getAttribute("src") === src);
      document.getElementById("lightbox-img").src = src;
      document.getElementById("lightbox-caption").innerText = src.split('/').pop();
      document.getElementById("lightbox").style.display = "flex";
    }}

    function closeLightbox() {{
      document.getElementById("lightbox").style.display = "none";
    }}

    function navigate(direction) {{
      if (currentIndex === -1) return;
      currentIndex += direction;
      if (currentIndex < 0) currentIndex = images.length - 1;
      if (currentIndex >= images.length) currentIndex = 0;
      const nextSrc = images[currentIndex].getAttribute("src");
      document.getElementById("lightbox-img").src = nextSrc;
      document.getElementById("lightbox-caption").innerText = nextSrc.split('/').pop();
    }}

    document.addEventListener("keydown", function(e) {{
      if (document.getElementById("lightbox").style.display === "flex") {{
        if (e.key === "ArrowRight") navigate(1);
        if (e.key === "ArrowLeft") navigate(-1);
        if (e.key === "Escape") closeLightbox();
      }}
    }});
  </script>
</body>
</html>
"""

# Generate each gallery page
# Generate each gallery page
for folder in os.listdir(source_dir):
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        images_html = ""
        for file in sorted(os.listdir(folder_path)):
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                rel_path = f'gallery_images/{folder}/{file}'
                images_html += f'<img src="{rel_path}" alt="{file}" onclick="showLightbox(\'{rel_path}\')">\n'

        page_name = folder.replace(" ", "-") + ".html"
        output_path = os.path.join(output_dir, page_name)

        with open(output_path, "w") as f:
            f.write(html_template.format(title=folder, images=images_html))

print("✅ Gallery pages generated.")
