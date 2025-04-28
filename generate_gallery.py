import os

# Path to your local images folder (adjust if needed)
images_folder = "images"

# List all files in the images folder
files = os.listdir(images_folder)

# Only keep image files
image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Sort files alphabetically (optional, but nice)
image_files.sort()

# Start generating HTML
for image in image_files:
    # Clean up the title (remove extension, replace underscores with spaces, capitalize words)
    title = os.path.splitext(image)[0].replace('_', ' ').title()

    # Build the HTML block
    block = f'''
<article>
    <a class="thumbnail" href="images/{image}" data-position="center center">
      <img src="images/{image}" alt="{title}" />
    </a>
    <h2>{title}</h2>
    <p>A journey into the unseen world captured by Ravensight.</p>
</article>
'''
    print(block)
