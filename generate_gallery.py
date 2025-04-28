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
<section id="thumbnails">
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
for filename in sorted(os.listdir(images_dir)):
    if os.path.splitext(filename)[1].lower() in valid_extensions:
        clean_title = filename.replace("_", " ").replace("-", " ").rsplit(".", 1)[0]
        articles += f'''
<article>
    <a class="thumbnail" href="{images_dir}/{filename}" data-position="center center">
      <img src="{images_dir}/{filename}" alt="{clean_title}" />
    </a>
    <h2>{clean_title}</h2>
    <p>A journey into the unseen world captured by Ravensight.</p>
</article>
'''

# Save to file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(header + articles + footer)

print("Gallery regenerated successfully!")
