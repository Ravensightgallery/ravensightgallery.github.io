import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Config
images_dir = "images"
output_file = "index.html"
valid_extensions = {".jpg", ".jpeg", ".png", ".gif"}

# Template pieces
header = '''<!DOCTYPE html>
<html>
<head>
  <title>Ravensight Gallery</title>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
  <link rel="stylesheet" href="assets/css/main.css" />
  <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
</head>
<body class="is-preload-0 is-preload-1 is-preload-2">
<div id="main">
<header id="header">
  <h1>Ravensight Gallery</h1>
  <p>Through the eyes of the raven, a world unseen is revealed.</p>
  <ul class="icons">
    <li><a href="#" class="icon brands fa-twitter"><span class="label">Twitter</span></a></li>
    <li><a href="#" class="icon brands fa-instagram"><span class="label">Instagram</span></a></li>
    <li><a href="#" class="icon brands fa-github"><span class="label">Github</span></a></li>
    <li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
  </ul>
</header>
<section id="directory">
'''

footer = '''
</section>
<footer id="footer">
  <ul class="copyright">
    <li>&copy; Ravensight Gallery.</li>
    <li>Design: <a href="http://html5up.net">HTML5 UP</a>.</li>
  </ul>
</footer>
</div>
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/browser.min.js"></script>
<script src="assets/js/breakpoints.min.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
'''

# Build gallery
articles = ""

for folder in sorted(os.listdir(images_dir)):
    folder_path = os.path.join(images_dir, folder)
    if os.path.isdir(folder_path):
        # Clean folder name for display
        clean_folder_name = folder.replace("-", " ").replace("_", " ").title()

        articles += f"<h2>{clean_folder_name}</h2>\n"

        for filename in sorted(os.listdir(folder_path)):
            if os.path.splitext(filename)[1].lower() in valid_extensions:
                clean_title = filename.replace("_", " ").replace("-", " ").rsplit(".", 1)[0]
                image_path = f"{images_dir}/{folder}/{filename}"

                articles += f'''
<article>
    <a class="thumbnail" href="{image_path}" data-position="center center">
      <img src="{image_path}" alt="{clean_title}" />
    </a>
    <h3>{clean_title}</h3>
</article>
'''

# Save to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(header + articles + footer)

print("Gallery regenerated successfully!")
